import stripe
from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Stripe APIキーを設定
stripe.api_key = settings.STRIPE_SECRET_KEY

# Stripeの支払いview
class CreateCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # herokuアプリの設定も加える
        YOUR_DOMAIN = 'http://127.0.0.1:8000/'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': 'price_1PKXSk00BXxPp9eq1ubxOxIU',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=YOUR_DOMAIN + '/checkout_success/',
            cancel_url=YOUR_DOMAIN + '/checkout_cancel/',
        )
        return redirect(checkout_session.url, code=303)