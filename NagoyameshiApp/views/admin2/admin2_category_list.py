from django.views.generic import ListView
from NagoyameshiApp.models.category import Category

# ================== 管理者（サイト運営側）画面 ==================

# カテゴリ管理
class CategoryListView(ListView):
    model = Category
    template_name = "NagoyameshiApp/admin2/category_list.html"
    