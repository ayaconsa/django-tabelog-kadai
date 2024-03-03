from django.views.generic import DeleteView
from NagoyameshiApp.models.category import Category
from django.urls import reverse_lazy



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('admin_category_list')
    template_name = "NagoyameshiApp/admin2/category_delete.html"
