from django.views.generic import TemplateView
from NagoyameshiApp.models.restaurant import Restaurant


# ================== 管理者（サイト運営側）画面 ==================

# レビュー確認ページ
class AdminReviewConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/admin2/admin_review_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 自店舗に対するレビュー情報を取得してテンプレートに渡す
        restaurant = Restaurant.objects.get(pk=self.kwargs['pk'])
        context['reviews'] = restaurant.get_reviews()
        context['restaurant_name'] = restaurant.name
        return context