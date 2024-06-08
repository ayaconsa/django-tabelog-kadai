from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.favorite import Favorite

class FavoriteToggleView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        user = request.user
        restaurant_id = kwargs.get('pk')
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        favorite, created = Favorite.objects.get_or_create(user=user, restaurant=restaurant)

        if not created:
            favorite.delete()
            status = 'unfavorited'
        else:
            status = 'favorited'

        return JsonResponse({'status': 'success', 'favorite_status': status})
