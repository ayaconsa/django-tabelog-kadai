from django.views.generic import TemplateView



# ================== 管理（店舗側）画面 ==================

# レビュー確認
class ReviewConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/manage/review_confirmation.html"
