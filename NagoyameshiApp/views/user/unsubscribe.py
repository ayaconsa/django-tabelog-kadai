from django.views.generic import TemplateView

# サブスク本当に解約しますか？（サブスク会員のみ）
class UnsubscribeView(TemplateView):
    template_name = "NagoyameshiApp/user/unsubscribe.html"
