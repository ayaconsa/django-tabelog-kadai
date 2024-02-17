from django.views.generic import TemplateView


# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# 会社概要
class CompanyOverviewView(TemplateView):
    template_name = "NagoyameshiApp/company_overview.html"
