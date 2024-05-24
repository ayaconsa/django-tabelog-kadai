import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# デバッグ用
print("Stripe Secret Key in view: ", settings.STRIPE_SECRET_KEY)

# Stripe APIキーを設定
stripe.api_key = settings.STRIPE_SECRET_KEY

# Stripeの支払いview
class CreateCheckoutSessionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://localhost:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'jpy',
                        'product_data': {
                            'name': 'Monthly Subscription',
                        },
                        'unit_amount': 30000,
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)