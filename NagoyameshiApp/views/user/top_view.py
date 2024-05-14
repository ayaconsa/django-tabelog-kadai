from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.category import Category
from django.db.models import Q

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# トップページ
class TopView(TemplateView):
    template_name = "NagoyameshiApp/user/top.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 店舗データの取得
        restaurants = Restaurant.objects.all()

        # カテゴリデータの取得
        categories = Category.objects.all()
        context['categories'] = categories

        # キーワード検索
        keyword = self.request.GET.get('keyword')
        if keyword:
            # 名前、カテゴリ、説明などのフィールドを検索する
            restaurants = restaurants.filter(
                Q(name__icontains=keyword) |
                Q(category__name__icontains=keyword) |
                Q(explanation__icontains=keyword) |
                Q(address__icontains=keyword) |
                Q(catch_copy__icontains=keyword)
            )
        
        # ジャンルで絞り込んだ場合
        genre = self.request.GET.get('genre')
        if genre:
            restaurants = Restaurant.objects.filter(category__name=genre)
        else:
            restaurants = Restaurant.objects.all()

        # 評価の高い順にレストランを取得し表示する（上位6件）
        context['top_rated_restaurants'] = Restaurant.get_top_rated_restaurants()[:6]
        context['latest_restaurants'] = Restaurant.get_latest_restaurants()[:6]

        # ようこそ〇〇さんを表示するために取得
        context['user'] = self.request.user

        return context
