from django.views.generic import TemplateView, DetailView
from NagoyameshiApp.models.restaurant import Restaurant



# ================== 管理者（サイト運営側）画面 ==================

# 店舗詳細ページ
class AdminRestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "NagoyameshiApp/admin2/admin_restaurant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 評価の平均と件数を取得
        average_score, review_count = self.object.get_average()
        context['average_score'] = average_score
        context['review_count'] = review_count
        
        # お気に入り登録件数を取得
        favorite_count = self.object.get_favorite_count()
        context['favorite_count'] = favorite_count
        
        return context