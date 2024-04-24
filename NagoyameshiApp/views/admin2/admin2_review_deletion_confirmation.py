from django.views.generic import DeleteView
from NagoyameshiApp.models.review import Review
from django.urls import reverse_lazy



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class ReviewDeletionConfirmationView(DeleteView):
    model = Review
    success_url = reverse_lazy('admin_review_confirmation')
    template_name = "NagoyameshiApp/admin2/admin_review_deletion_confirmation.html"
