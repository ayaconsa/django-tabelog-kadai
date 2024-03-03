from django.views.generic import ListView
from NagoyameshiApp.models.custom_user import CustomUser


# ================== 管理者（サイト運営側）画面 ==================

# 会員一覧
class UserListView(ListView):
    model = CustomUser
    template_name = "NagoyameshiApp/admin2/user_list.html"
