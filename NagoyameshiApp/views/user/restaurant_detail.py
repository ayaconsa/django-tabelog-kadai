from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant
from NagoyameshiApp.models.review import Review

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# 店舗詳細（→ 予約とレビューを会員限定にするにはどうしたらいいのか）
class RestaurantDetailView(TemplateView):
    template_name = "NagoyameshiApp/user/restaurant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # URLからrestaurant.pkを取得
        restaurant_id = self.kwargs.get('pk')

        # pkに対応する店舗を取得してcontextに追加
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        context['restaurant'] = restaurant

        # レビューデータを取得してcontextに追加
        reviews = Review.objects.filter(restaurant=restaurant)
        context['reviews'] = reviews

        # ユーザー名の取得
        user_names = [review.user for review in reviews]
        context['user_names'] = user_names

        # 評価の平均と件数を取得
        average_score, review_count = restaurant.get_average()
        context['average_score'] = average_score
        context['review_count'] = review_count

        return context
    
