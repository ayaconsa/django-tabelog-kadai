from django.views.generic import TemplateView



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminTopView(TemplateView):
    template_name = "NagoyameshiApp/admin2/admin_top.html"
