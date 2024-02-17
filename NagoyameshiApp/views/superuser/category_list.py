from django.views.generic import TemplateView

# ================== 管理者（サイト運営側）画面 ==================

# カテゴリ管理
class CategoryListView(TemplateView):
    template_name = "NagoyameshiApp/admin/category_list.html"
