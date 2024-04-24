from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# トップページ
class TopView(TemplateView):
    template_name = "NagoyameshiApp/user/top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 評価の高い順にレストランを取得し表示する（上位6件）
        context['top_rated_restaurants'] = Restaurant.get_top_rated_restaurants()[:6]
        context['latest_restaurants'] = Restaurant.get_latest_restaurants()[:6]
        return context
