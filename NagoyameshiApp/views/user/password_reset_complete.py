from django.views.generic import TemplateView

class PasswordResetCompleteView(TemplateView):
    template_name = 'NagoyameshiApp/user/password_reset_complete.html'