from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from NagoyameshiApp.models.custom_user import CustomUser

# 退会（会員のみ）
class AccountDeleteView(LoginRequiredMixin, View):
    template_name = "NagoyameshiApp/user/account_delete.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    # 退会してもレコードは削除しない（is_activeフラグを変える）
    def post(self, request, *args, **kwargs):
        user = request.user
        user.subscription = False
        user.cancellation_date = timezone.now().date()
        user.is_active = False  # アカウントを無効化
        user.save()
        return redirect('top')
