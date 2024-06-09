from django.views.generic import ListView
from NagoyameshiApp.models.restaurant import Restaurant
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：店舗一覧
class AdminRestaurantListView(ListView):
    model = Restaurant
    template_name = "NagoyameshiApp/admin2/admin_restaurant_list.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
