from django.views.generic import TemplateView




# ================== 管理（店舗側）画面 ==================


# 管理者（店舗）トップページ
class ManageTopView(TemplateView):
    template_name = "NagoyameshiApp/manage/manage_top.html"
