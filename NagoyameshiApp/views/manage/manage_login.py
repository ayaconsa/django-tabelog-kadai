from django.views.generic import TemplateView


# ================== 管理（店舗側）画面 ==================

# 管理者（店舗）ログイン
class ManageLoginView(TemplateView):
    template_name = "NagoyameshiApp/manage/manage_login.html"
