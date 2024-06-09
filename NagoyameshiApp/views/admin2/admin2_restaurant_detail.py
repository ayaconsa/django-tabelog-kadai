from django.views.generic import TemplateView, DetailView
from NagoyameshiApp.models.restaurant import Restaurant
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：店舗詳細
class AdminRestaurantDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Restaurant
    template_name = "NagoyameshiApp/admin2/admin_restaurant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 評価の平均と件数を取得
        average_score, review_count = self.object.get_average()
        context['average_score'] = average_score
        context['review_count'] = review_count
        
        # お気に入り登録件数を取得
        favorite_count = self.object.get_favorite_count()
        context['favorite_count'] = favorite_count
        
        return context
    
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
