from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from NagoyameshiApp.models.custom_user import CustomUser

class AccountCreateDoneView(View):
    def get(self, request, *args, **kwargs):
        email = request.session.get('user_email')
        return render(request, 'NagoyameshiApp/user/account_create_done.html', {'email': email})
    
    def post(self, request, *args, **kwargs):
        email = request.session.get('user_email')
        if email:
            user = get_object_or_404(CustomUser, email=email)
            if not user.is_active:
                current_site = get_current_site(request)
                subject = 'アカウントを有効化してください（Nagoyameshi）'
                message = render_to_string('NagoyameshiApp/user/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                send_mail(subject, message, 'from@example.com', [user.email], fail_silently=False, html_message=message)
                return redirect('account_create_done')
            return redirect('account_create')