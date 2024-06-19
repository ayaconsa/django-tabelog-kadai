from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.urls import reverse
from urllib.parse import urlencode

# 店舗一覧（全員）
class RestaurantListView(TemplateView):
    template_name = "NagoyameshiApp/user/restaurant_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 店舗データの取得
        restaurants = Restaurant.objects.all()

        # 検索
        keyword = self.request.GET.get('keyword')
        genre = self.request.GET.get('genre')
        price_min = self.request.GET.get('list_price_min')
        price_max = self.request.GET.get('list_price_max')

        if keyword:
            # 名前、カテゴリ、説明などのフィールドを検索する（カテゴリは孫引きになっている）
            restaurants = restaurants.filter(
                Q(name__icontains=keyword) |
                Q(category__name__icontains=keyword) |
                Q(explanation__icontains=keyword) |
                Q(address__icontains=keyword) |
                Q(catch_copy__icontains=keyword)
            )

        if genre:
            restaurants = restaurants.filter(category__name=genre)

        if price_min and price_max:
            restaurants = restaurants.filter(price_min__gte=price_min, price_max__lte=price_max)

        # 並び替えオプション
        sort_option = self.request.GET.get('sort')
        if sort_option == '価格が安い順':
            restaurants = restaurants.order_by('price_min')
        elif sort_option == '価格が高い順':
            restaurants = restaurants.order_by('-price_min')
        elif sort_option == '予約数順':
            restaurants = restaurants.annotate(booking_count=Count('booking')).order_by('-booking_count')
        else: # デフォルトは掲載日が新しい順
            restaurants = restaurants.order_by('-created_at')

        # ページネーション
        paginator = Paginator(restaurants, self.paginate_by)
        page_number = self.request.GET.get('page') # ページ番号の取得
        page_obj = paginator.get_page(page_number)

        # 検索条件を含むクエリパラメータの作成
        query_params = {
            'keyword': keyword,
            'genre': genre,
            'list_price_min': price_min,
            'list_price_max': price_max,
            'sort': sort_option
        }

        # ページネーションオブジェクトにクエリパラメータを追加
        page_obj.query_params = urlencode(query_params)

        context['restaurants'] = page_obj
        context['hit_restaurants_number'] = paginator.count # 検索された店舗数
        context['sort_options'] = [
            ('掲載日が新しい順', '新しい順'),
            ('価格が安い順', '価格が安い順'),
            ('価格が高い順', '価格が高い順'),
            ('予約数順', '予約数順'),
        ]
        context['sort_option'] = sort_option
        return context

        
