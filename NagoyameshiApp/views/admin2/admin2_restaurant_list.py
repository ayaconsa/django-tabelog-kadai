from django.views.generic import ListView
from NagoyameshiApp.models.restaurant import Restaurant



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminRestaurantListView(ListView):
    model = Restaurant
    template_name = "NagoyameshiApp/admin2/admin_restaurant_list.html"
