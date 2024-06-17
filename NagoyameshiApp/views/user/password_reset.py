from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.tokens import default_token_generator
from NagoyameshiApp.forms import CustomPasswordResetForm

class PasswordResetView(FormView):
    template_name =  'NagoyameshiApp/user/password_reset.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        form.save(
            request=self.request,
            use_https=self.request.is_secure(),
            token_generator=default_token_generator,
            from_email='from@example.com',
            email_template_name='NagoyameshiApp/user/password_reset_email.html',
        )
        return super().form_valid(form)