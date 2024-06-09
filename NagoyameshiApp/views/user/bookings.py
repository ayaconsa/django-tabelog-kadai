from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.booking import Booking

# 予約一覧（有料会員のみ）
class BookingsView(LoginRequiredMixin, TemplateView):
    template_name = "NagoyameshiApp/user/bookings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        bookings = Booking.objects.filter(user=user)
        context['bookings'] = bookings
        return context
    
