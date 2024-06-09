from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.review import Review
from django.urls import reverse
from django.core.paginator import Paginator
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)

# レビュー一覧（会員のみ）
class ReviewsView(TemplateView):
    template_name = "NagoyameshiApp/user/reviews.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant_id = self.kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        context['restaurant'] = restaurant

        reviews_list = Review.objects.filter(restaurant=restaurant).order_by('-created_at')
        paginator = Paginator(reviews_list, 5)
        page = self.request.GET.get('page')
        reviews = paginator.get_page(page)
        context['reviews'] = reviews

        return context

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return render(request, 'NagoyameshiApp/user/login_required.html')
        return super().dispatch(request, *args, **kwargs)
