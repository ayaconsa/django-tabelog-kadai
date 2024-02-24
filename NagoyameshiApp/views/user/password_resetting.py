from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# **************** 会員（非サブスク会員含む）のみ表示 *****************


# パスワード再設定ページ
class PasswordResettingView(TemplateView):
    template_name = "NagoyameshiApp/user/password_resetting.html"
