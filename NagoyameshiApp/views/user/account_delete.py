from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.custom_user import CustomUser

# **************** 退会ページ *****************

class AccountDeleteView(LoginRequiredMixin, View):
    template_name = "NagoyameshiApp/user/account_delete.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        user.delete()
        return redirect('top')