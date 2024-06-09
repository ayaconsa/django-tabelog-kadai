from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# ログアウト（会員のみ）
# 継承の順番重要
# LoginRequiredMixinはログイン状態でのみ表示されるview → 非ログイン時はログイン画面に遷移
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "NagoyameshiApp/user/logout.html"
    next_page = reverse_lazy('top')
