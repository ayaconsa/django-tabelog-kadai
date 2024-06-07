from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.review import Review
from django.urls import reverse
from django.core.paginator import Paginator
import logging

logger = logging.getLogger(__name__)

# レビュー
class ReviewsView(TemplateView):
    template_name = "NagoyameshiApp/user/reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        context['restaurant'] = restaurant

        reviews_list = Review.get_newest_reviews(restaurant)
        paginator = Paginator(reviews_list, 5)
        page_number = self.request.GET.get('page')
        reviews = paginator.get_page(page_number)
        context['reviews'] = reviews

        user_names = [review.user for review in reviews]
        context['user_names'] = user_names

        average_score, review_count = restaurant.get_average()
        context['average_score'] = average_score
        context['review_count'] = review_count

        return context
