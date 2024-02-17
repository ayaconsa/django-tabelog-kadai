from django.views.generic import TemplateView



# ================== 管理（店舗側）画面 ==================

# 予約確認
class BookingConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/manage/booking_confirmation.html"
