from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ...models.user import User



# **************** サブスク会員のみ表示 *****************

# 会員情報
class AccountInfoView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = "NagoyameshiApp/acount_info.html"
