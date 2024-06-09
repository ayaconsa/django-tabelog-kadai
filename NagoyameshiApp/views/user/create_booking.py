from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.forms import BookingForm
from django.urls import reverse
import logging

logger = logging.getLogger(__name__)

# 予約（有料会員のみ）
class CreateBookingView(TemplateView):
    template_name = "NagoyameshiApp/user/create_booking.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        context['restaurant'] = restaurant

        if self.request.user.is_authenticated and self.request.user.subscription:
            context['booking_form'] = BookingForm()

        return context

    def post(self, request, *args, **kwargs):
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        if request.user.is_authenticated and request.user.subscription:
            form = BookingForm(request.POST)
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