from django.views.generic import TemplateView


# ================== 管理者（サイト運営側）画面 ==================

# 管理者（サイト運営者）ログイン
class AdminLoginView(TemplateView):
    template_name = "NagoyameshiApp/admin2/admin_login.html"
