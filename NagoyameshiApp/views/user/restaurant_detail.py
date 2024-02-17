from django.views.generic import TemplateView
from ...models.restaurant import Restaurant

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# 店舗詳細（→ 予約とレビューを会員限定にするにはどうしたらいいのか）
class RestaurantDetailView(TemplateView):
    model = Restaurant
    template_name = "NagoyameshiApp/restaurant_detail.html"
