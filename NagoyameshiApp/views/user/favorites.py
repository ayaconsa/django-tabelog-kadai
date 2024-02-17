from django.views.generic import TemplateView


# **************** サブスク会員のみ表示 *****************

# お気に入り一覧
class FavoritesView(TemplateView):
    template_name = "NagoyameshiApp/favorites.html"
