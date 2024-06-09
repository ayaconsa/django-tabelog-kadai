from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：売上集計
class SalesView(TemplateView):
    template_name = "NagoyameshiApp/admin2/sales.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
