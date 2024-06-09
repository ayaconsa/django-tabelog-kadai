from django.views.generic import TemplateView

# アカウント削除（会員のみ）
class DeleteAccountView(TemplateView):
    template_name = "NagoyameshiApp/user/delete_account.html"
