from django.views.generic import TemplateView
from NagoyameshiApp.models.review import Review
from NagoyameshiApp.models.favorite import Favorite
from NagoyameshiApp.models.booking import Booking



# **************** サブスク会員のみ表示 *****************


# 予約一覧
class BookingsView(TemplateView):
    template_name = "NagoyameshiApp/user/bookings.html"
