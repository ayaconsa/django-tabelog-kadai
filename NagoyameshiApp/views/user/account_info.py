from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.custom_user import CustomUser



# **************** サブスク会員のみ表示 *****************

# 会員情報
class AccountInfoView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "NagoyameshiApp/user/account_info.html"
