from django.views.generic import DeleteView
from NagoyameshiApp.models.review import Review
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect

# 管理者：レビュー削除確認
class ReviewDeletionConfirmationView(DeleteView):
    model = Review
    template_name = "NagoyameshiApp/admin2/admin_review_deletion_confirmation.html"

    def get_success_url(self):
        # 削除したレビューのpkを取得し、それを使用して成功時のURLを生成
        restaurant_pk = self.object.restaurant.pk
        return reverse_lazy('admin_review_confirmation', kwargs={'pk': restaurant_pk})

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト
