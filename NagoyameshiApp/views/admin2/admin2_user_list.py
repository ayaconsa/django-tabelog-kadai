from django.views.generic import ListView
from NagoyameshiApp.models.custom_user import CustomUser
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：会員一覧
class UserListView(ListView):
    model = CustomUser
    template_name = "NagoyameshiApp/admin2/user_list.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
