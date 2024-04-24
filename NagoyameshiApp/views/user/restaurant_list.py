from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant
from django.core.paginator import Paginator

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

        
