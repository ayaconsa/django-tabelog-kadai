from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
# from NagoyameshiApp.models.custom_user import CustomUser

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************


# ログイン
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "NagoyameshiApp/user/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = context['form']
        for v in form.fields.values():
            v.label_suffix = ""
            
        return context

    # def login(request):
    #     email = request.POST["email"]
    #     password = request.POST["password"]

    #     if CustomUser.objects.filter(email=email).exists() and CustomUser.objects.get(email=email).check_password(password):
