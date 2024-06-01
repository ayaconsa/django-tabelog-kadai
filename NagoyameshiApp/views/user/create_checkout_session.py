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
        # YOUR_DOMAINが開発環境と本番環境で変わるようにsettings.pyに記述
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': 'price_1PKXSk00BXxPp9eq1ubxOxIU',
                    'quantity': 1,
                },
            ],
            mode='subscription',
            success_url=f"{settings.YOUR_DOMAIN}/checkout_success/?session_id={{CHECKOUT_SESSION_ID}}&user_id={request.user.id}",
            cancel_url=f"{settings.YOUR_DOMAIN}/checkout_cancel/",
        )
        return redirect(checkout_session.url, code=303)