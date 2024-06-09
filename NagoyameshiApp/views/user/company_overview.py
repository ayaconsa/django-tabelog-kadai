from django.views.generic import TemplateView

# 会社概要（全員）
class CompanyOverviewView(TemplateView):
    template_name = "NagoyameshiApp/user/company_overview.html"
