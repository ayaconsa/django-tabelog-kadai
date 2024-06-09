from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：ユーザー数管理（未実装）
class UserNumberView(UserPassesTestMixin, LoginRequiredMixin, TemplateView):
    template_name = "NagoyameshiApp/admin2/user_number.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
