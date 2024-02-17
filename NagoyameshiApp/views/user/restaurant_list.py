from django.views.generic import TemplateView
from ...models.restaurant import Restaurant

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# 店舗一覧
class RestaurantListView(TemplateView):
    model = Restaurant
    template_name = "NagoyameshiApp/restaurant_list.html"
    # context_object_name = ''
    # テンプレートに渡されるオブジェクト名を任意のものに指定できる
    paginate_by = 10
