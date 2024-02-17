from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************


# ログイン
class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "NagoyameshiApp/login.html"
