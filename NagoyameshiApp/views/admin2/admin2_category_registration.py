from typing import Any
from django.views.generic import CreateView
from NagoyameshiApp.models.category import Category
from django import forms


# ================== 管理者（サイト運営側）画面 ==================


# カテゴリ登録画面
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
