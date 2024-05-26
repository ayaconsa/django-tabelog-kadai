import stripe
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class CancelSubscriptionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user = request.user
        # Stripeサブスクリプションの解約
        if user.stripe_subscription_id:
            try:
                stripe.Subscription.delete(user.stripe_subscription_id)
            except stripe.error.StripeError as e:
                return HttpResponse(status=400)
            
        user.subscription = False
        user.save()
        return redirect('subscription_guide') 