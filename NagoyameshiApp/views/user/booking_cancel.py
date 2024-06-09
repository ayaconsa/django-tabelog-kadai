from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.booking import Booking

# 予約キャンセル（有料会員のみ）
class BookingCancelView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        booking_id = kwargs.get('pk')
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.delete()
        return redirect('bookings')
