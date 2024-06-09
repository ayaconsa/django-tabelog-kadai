from django.views.generic import UpdateView
from NagoyameshiApp.models.restaurant import Restaurant
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：店舗編集
class AdminRestaurantEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Restaurant
    fields = '__all__'
    
    template_name = "NagoyameshiApp/admin2/admin_restaurant_edit.html"
    
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
