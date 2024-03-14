from django.views.generic.edit import CreateView
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.forms import CustomUserForm
from django.contrib.auth.hashers import make_password

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# アカウントの新規登録

class CreateAccountView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "NagoyameshiApp/user/account_create.html"
    
    def form_valid(self, form):
        # パスワードをハッシュ化
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)
