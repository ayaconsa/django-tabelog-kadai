from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ...models.restaurant import Restaurant


# ================== 管理（店舗側）画面 ==================

# 店舗情報（登録・編集・削除）
class RestaurantInfoView(LoginRequiredMixin, TemplateView):
    model = Restaurant
    fields = '__all__' #フィールド内全件指定
    # fields = ["title", "image", "text"]のように指定することも可
    template_name = "NagoyameshiApp/manage/restaurant_info.html"
