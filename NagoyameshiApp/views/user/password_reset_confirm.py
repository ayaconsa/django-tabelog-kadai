from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from NagoyameshiApp.models.custom_user import CustomUser

class PasswordResetConfirmView(FormView):
    template_name = 'NagoyameshiApp/user/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        uidb64 = self.kwargs.get('uidb64')
        token = self.kwargs.get('token')

        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            user = None

        self.user = user
        kwargs['user'] = user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)