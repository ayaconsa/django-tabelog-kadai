from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant


# ================== 管理者（サイト運営側）画面 ==================

# 予約確認ページ
class AdminBookingConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/admin2/admin_booking_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 自店舗に対する予約情報を取得してテンプレートに渡す
        restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        context['bookings'] = restaurant.get_booking_data()
        context['restaurant_name'] = restaurant.name
        return context