from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# ログイン（非会員のみ）
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "NagoyameshiApp/user/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = context['form']
        for v in form.fields.values():
            v.label_suffix = ""
            
        return context
