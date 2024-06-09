from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# パスワード再設定ページ（未実装）
class PasswordResettingView(TemplateView):
    template_name = "NagoyameshiApp/user/password_resetting.html"
