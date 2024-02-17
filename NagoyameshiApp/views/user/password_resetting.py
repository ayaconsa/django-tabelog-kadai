from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


# **************** 会員（非サブスク会員含む）のみ表示 *****************


# パスワード再設定ページ
class PasswordResettingView(LoginRequiredMixin, TemplateView):
    template_name = "NagoyameshiApp/password_resetting.html"
