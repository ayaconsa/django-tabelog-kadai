from typing import Any
from django.views.generic import CreateView
from NagoyameshiApp.models.category import Category
from django import forms
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：カテゴリ登録
class CategoryRegistrationView(CreateView):
    model = Category
    fields = '__all__'
    
    template_name = "NagoyameshiApp/admin2/category_registration.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = context['form']
        for v in form.fields.values():
            v.label_suffix = ""
                
        return context

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
