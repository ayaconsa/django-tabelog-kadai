from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


# **************** 会員（非サブスク会員含む）のみ表示 *****************

# ログアウト
# 継承の順番重要
# LoginRequiredMixinはログイン状態でのみ表示されるview → 非ログイン時はログイン画面に遷移
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "NagoyameshiApp/logout.html"
