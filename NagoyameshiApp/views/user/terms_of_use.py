from django.views.generic import TemplateView


# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# 利用規約
class TermsOfUseView(TemplateView):
    template_name = "NagoyameshiApp/terms_of_use.html"
