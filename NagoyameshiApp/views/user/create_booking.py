from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.forms import BookingForm
from django.urls import reverse
from NagoyameshiApp.models.booking import Booking
import logging
import json

logger = logging.getLogger(__name__)

# 予約（有料会員のみ）
class CreateBookingView(TemplateView):
    template_name = "NagoyameshiApp/user/create_booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # close_dayの内容を確認	
        close_days = restaurant.close_day.split(', ')	
        logger.debug(f'close_days: {close_days}')

        context['restaurant'] = restaurant

        context['close_day'] = json.dumps([self.day_to_number(day) for day in close_days])
        context['open_time'] = restaurant.open_time
        context['close_time'] = restaurant.close_time


        if self.request.user.is_authenticated and self.request.user.subscription:
            context['booking_form'] = BookingForm()

        return context

    def post(self, request, *args, **kwargs):
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)


        if request.user.is_authenticated and request.user.subscription:
            form = BookingForm(request.POST, instance=Booking(restaurant=restaurant))
            if form.is_valid():
                booking = form.save(commit=False)
                booking.user = request.user
                booking.restaurant = restaurant
                booking.save()
                logger.info("Booking successful, redirecting to booking_success")
                return redirect(reverse('booking_success'))
            else:
                logger.warning("Booking form is invalid: %s", form.errors)

        logger.warning("Booking failed, reloading the page")
        return self.get(request, *args, **kwargs)

    def day_to_number(self, day):
        days = {
            '月曜日': 1,
            '火曜日': 2,
            '水曜日': 3,
            '木曜日': 4,
            '金曜日': 5,
            '土曜日': 6,
            '日曜日': 0
        }
        return days.get(day, -1)