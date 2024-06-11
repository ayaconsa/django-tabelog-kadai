from django.shortcuts import render, redirect
from django.views.generic.edit import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from NagoyameshiApp.forms import CustomUserForm

# アカウント登録（非会員のみ）
class AccountCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        return render(request, 'NagoyameshiApp/user/account_create.html')

    def post(self, request, *args, **kwargs):
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            subject = 'アカウントを有効化してください'
            message = render_to_string('NagoyameshiApp/user/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            send_mail(subject, message, 'from@example.com', [user.email], fail_silently=False, html_message=message)
            return redirect('account_create_done')
        return render(request, 'NagoyameshiApp/user/account_create.html', {'form': form})