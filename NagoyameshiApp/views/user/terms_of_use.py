from django.views.generic import TemplateView

# 利用規約（全員）
class TermsOfUseView(TemplateView):
    template_name = "NagoyameshiApp/user/terms_of_use.html"
