from django.views.generic import TemplateView

class PasswordResetDoneView(TemplateView):
    template_name = 'NagoyameshiApp/user/password_reset_done.html'