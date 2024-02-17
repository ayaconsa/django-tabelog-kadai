from django.views.generic import TemplateView

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# トップページ
class TopView(TemplateView):
    template_name = "NagoyameshiApp/top.html"
