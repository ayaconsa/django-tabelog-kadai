from django.views.generic import TemplateView

# 予約完了ページ
class BookingSuccessView(TemplateView):
    template_name = "NagoyameshiApp/user/booking_success.html"
