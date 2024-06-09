from django.views.generic import ListView
from NagoyameshiApp.models.category import Category
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：カテゴリ一覧
class CategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category
    template_name = "NagoyameshiApp/admin2/category_list.html"
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
