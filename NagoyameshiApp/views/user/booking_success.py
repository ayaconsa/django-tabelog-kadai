from django.views.generic import TemplateView

# 予約完了（有料会員のみ）
class BookingSuccessView(TemplateView):
    template_name = "NagoyameshiApp/user/booking_success.html"
