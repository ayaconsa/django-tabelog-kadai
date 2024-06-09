from django.views.generic import TemplateView

# サブスク案内（有料会員以外）
class SubscriptionGuideView(TemplateView):
    template_name = "NagoyameshiApp/user/subscription_guide.html"