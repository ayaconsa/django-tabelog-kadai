from django.shortcuts import render, redirect
from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from NagoyameshiApp.forms import EmailChangeForm

class EmailChangeRequestView(View):
    def get(self, request, *args, **kwargs):
        form = EmailChangeForm()
        return render(request, 'NagoyameshiApp/user/email_change.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = EmailChangeForm(request.POST)
        if form.is_valid():
            new_email = form.cleaned_data['new_email']
            current_site = get_current_site(request)
            subject = 'メールアドレス変更の確認（nagoyameshi）'
            message = render_to_string('NagoyameshiApp/user/email_change_activation.html', {
                'user': request.user,
                'domain': current_site.domain,
                'new_email': new_email,
                'uid': urlsafe_base64_encode(force_bytes(request.user.pk)),
                'token': default_token_generator.make_token(request.user),
            })
            # 新しいメールアドレスをURLに直接渡すのではなく、クエリパラメータとして渡す
            activation_link = f"http://{current_site.domain}/email_change/activate/{urlsafe_base64_encode(force_bytes(request.user.pk))}/{default_token_generator.make_token(request.user)}/?new_email={new_email}"
            send_mail(subject, message, 'from@example.com', [new_email], fail_silently=False, html_message=message)
            return redirect('email_change_done')
        return render(request, 'NagoyameshiApp/user/email_change.html', {'form': form})