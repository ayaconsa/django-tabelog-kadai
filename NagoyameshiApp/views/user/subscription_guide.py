from django.views.generic import TemplateView



# サブスク案内
class SubscriptionGuideView(TemplateView):
    template_name = "NagoyameshiApp/subscription_guide.html"
