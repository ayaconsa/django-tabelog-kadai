from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：予約確認
class AdminBookingConfirmationView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "NagoyameshiApp/admin2/admin_booking_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 自店舗に対する予約情報を取得してテンプレートに渡す
        restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        context['bookings'] = restaurant.get_booking_data()
        context['restaurant_name'] = restaurant.name
        return context
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
