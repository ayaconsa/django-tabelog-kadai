from django.views.generic import DeleteView
from NagoyameshiApp.models.restaurant import Restaurant
from django.urls import reverse_lazy



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminRestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('admin_restaurant_list')
    template_name = "NagoyameshiApp/admin2/admin_restaurant_delete.html"
