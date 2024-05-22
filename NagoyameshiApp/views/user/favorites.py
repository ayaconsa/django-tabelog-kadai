from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.favorite import Favorite

# **************** サブスク会員のみ表示 *****************

# お気に入り一覧
class FavoritesView(LoginRequiredMixin, TemplateView):
    template_name = "NagoyameshiApp/user/favorites.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        favorites = Favorite.objects.filter(user=user)
        context['favorites'] = favorites
        return context
