from django.views.generic import TemplateView



# ================== 管理者（サイト運営側）画面 ==================

# 売り上げ集計ページ
class SalesView(TemplateView):
    template_name = "NagoyameshiApp/admin/sales.html"
