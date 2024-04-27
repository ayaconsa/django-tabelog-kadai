from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant
from django.core.paginator import Paginator
from django.db.models import Q

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# 店舗一覧
class RestaurantListView(TemplateView):
    template_name = "NagoyameshiApp/user/restaurant_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 店舗データの取得
        restaurants = Restaurant.objects.all()

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

        # ジャンル検索
        genre = self.request.GET.get('genre')
        if genre:
            restaurants = restaurants.filter(category__name=genre)

        # 予算検索
        price_min = self.request.GET.get('list_price_min')
        price_max = self.request.GET.get('list_price_max')
        if price_min and price_max:
            restaurants = restaurants.filter(price_min__gte=price_min, price_max__lte=price_max)

        # ページネーション
        paginator = Paginator(restaurants, self.paginate_by)
        page_number = self.request.GET.get('page') # ページ番号の取得
        page_obj = paginator.get_page(page_number)

        context['restaurants'] = page_obj
        context['hit_restaurants_number'] = paginator.count # 検索された店舗数

        # 並び替えオプション
        context['sort_options'] = [
            ('掲載日が新しい順', '新しい順'),
            ('価格が安い順', '価格が安い順'),
            ('価格が高い順', '価格が高い順'),
            ('予約数順', '予約数順'),
        ]

        return context

        
