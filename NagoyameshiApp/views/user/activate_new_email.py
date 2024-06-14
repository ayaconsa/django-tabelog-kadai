from django.shortcuts import render, redirect
from django.views import View
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from NagoyameshiApp.models.custom_user import CustomUser

class ActivateNewEmailView(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        new_email = request.GET.get('new_email')
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None
        
        if user is not None and default_token_generator.check_token(user, token):
            user.email = new_email
            user.save()
            return redirect('email_change_complete')
        else:
            return render(request, 'NagoyameshiApp/user/account_activation_invalid.html')