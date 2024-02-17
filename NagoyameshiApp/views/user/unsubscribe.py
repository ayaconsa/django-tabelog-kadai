from django.views.generic import TemplateView



# **************** サブスク会員のみ表示 *****************

# サブスク解約
class UnsubscribeView(TemplateView):
    template_name = "NagoyameshiApp/unsubscribe.html"
