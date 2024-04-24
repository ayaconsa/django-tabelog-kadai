from django.views.generic import DeleteView
from NagoyameshiApp.models.review import Review
from django.urls import reverse_lazy



# ================== 管理者（サイト運営側）画面 ==================


# 投稿削除確認ページ
class ReviewDeletionConfirmationView(DeleteView):
    model = Review
    template_name = "NagoyameshiApp/admin2/admin_review_deletion_confirmation.html"

    def get_success_url(self):
        # 削除したレビューのpkを取得し、それを使用して成功時のURLを生成
        restaurant_pk = self.object.restaurant.pk
        return reverse_lazy('admin_review_confirmation', kwargs={'pk': restaurant_pk})
