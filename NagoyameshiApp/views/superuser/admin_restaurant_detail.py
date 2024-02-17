from django.views.generic import TemplateView



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminRestaurantDetailView(TemplateView):
    template_name = "NagoyameshiApp/admin/admin_restaurant_detail.html"
