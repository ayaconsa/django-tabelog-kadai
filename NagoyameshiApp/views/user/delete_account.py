from django.views.generic import TemplateView


# **************** 会員（非サブスク会員含む）のみ表示 *****************


# アカウント削除
class DeleteAccountView(TemplateView):
    template_name = "NagoyameshiApp/delete_account.html"
