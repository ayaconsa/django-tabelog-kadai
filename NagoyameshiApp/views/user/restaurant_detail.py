from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.review import Review
from NagoyameshiApp.forms import BookingForm
from django.urls import reverse

import logging

logger = logging.getLogger(__name__)

# 店舗詳細
class RestaurantDetailView(TemplateView):
    template_name = "NagoyameshiApp/user/restaurant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # URLからrestaurant.pkを取得
        restaurant_id = self.kwargs.get('pk')

        # pkに対応する店舗を取得してcontextに追加
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        context['restaurant'] = restaurant

        # レビューデータを取得してcontextに追加
        reviews = Review.objects.filter(restaurant=restaurant)
        context['reviews'] = reviews

        # ユーザー名の取得
        user_names = [review.user for review in reviews]
        context['user_names'] = user_names

        # 評価の平均と件数を取得
        average_score, review_count = restaurant.get_average()
        context['average_score'] = average_score
        context['review_count'] = review_count

        # 予約フォームを追加
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
