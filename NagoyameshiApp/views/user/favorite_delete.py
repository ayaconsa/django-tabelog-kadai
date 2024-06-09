from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.favorite import Favorite

# お気に入り削除（有料会員のみ）
class FavoriteDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        favorite_id = kwargs.get('pk')
        favorite = get_object_or_404(Favorite, id=favorite_id, user=request.user)
        favorite.delete()
        return redirect('favorites')
