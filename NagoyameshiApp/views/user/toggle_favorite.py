from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.favorite import Favorite
import json

class ToggleFavoriteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            restaurant_id = data.get('restaurant_id')
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

        user = request.user
        if not user.subscription:
            return JsonResponse({'error': 'Subscription required'}, status=403)

        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return JsonResponse({'error': 'Restaurant not found'}, status=404)

        favorite, created = Favorite.objects.get_or_create(user=user, restaurant=restaurant)
        if not created:
            favorite.delete()
            return JsonResponse({'status': 'unfavorited'})
        return JsonResponse({'status': 'favorited'})
