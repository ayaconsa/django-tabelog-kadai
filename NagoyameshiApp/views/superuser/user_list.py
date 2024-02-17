from django.views.generic import TemplateView


# ================== 管理者（サイト運営側）画面 ==================

# 会員一覧
class UserListView(TemplateView):
    template_name = "NagoyameshiApp/admin/user_list.html"
