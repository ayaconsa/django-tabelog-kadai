from django.views.generic import DeleteView
from NagoyameshiApp.models.restaurant import Restaurant
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：店舗削除
class AdminRestaurantDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Restaurant
    success_url = reverse_lazy('admin_restaurant_list')
    template_name = "NagoyameshiApp/admin2/admin_restaurant_delete.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
