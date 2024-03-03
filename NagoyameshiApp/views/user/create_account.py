from django.views.generic.edit import CreateView
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.forms import CustomUserForm

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# アカウントの新規登録

class CreateAccountView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    template_name = "NagoyameshiApp/user/account_create.html"
    
