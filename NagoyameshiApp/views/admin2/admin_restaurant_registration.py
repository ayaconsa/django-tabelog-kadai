from typing import Any
from django.views.generic import CreateView
from NagoyameshiApp.models.restaurant import Restaurant


# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminRestaurantRegistrationView(CreateView):
    model = Restaurant
    fields = '__all__'
    
    template_name = "NagoyameshiApp/admin2/admin_restaurant_registration.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = context['form']
        for v in form.fields.values():
            v.label_suffix = ""
        
        name = form.fields['name']
        name.widget.attrs = {"placeholder":"店舗名を入力してください"}
        
        return context
