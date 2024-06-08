from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.favorite import Favorite
import logging

logger = logging.getLogger(__name__)

# 店舗詳細
class RestaurantDetailView(TemplateView):
    template_name = "NagoyameshiApp/user/restaurant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        context['restaurant'] = restaurant
        average_score, review_count = restaurant.get_average()
        context['average_score'] = average_score
        context['review_count'] = review_count

        # ユーザーのお気に入り状態をチェック
        user = self.request.user
        if user.is_authenticated:
            is_favorite = Favorite.objects.filter(user=user, restaurant=restaurant).exists()
            context['is_favorite'] = is_favorite

        return context