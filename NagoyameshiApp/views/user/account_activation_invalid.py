from django.views.generic import TemplateView

class AccountActivationInvalidView(TemplateView):
    template_name = 'NagoyameshiApp/user/account_activation_invalid.html'
