from django.views.generic import TemplateView


# **************** サブスク会員のみ表示 *****************


# 予約一覧
class BookingsView(TemplateView):
    template_name = "NagoyameshiApp/bookings.html"
