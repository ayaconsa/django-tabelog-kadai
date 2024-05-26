import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from NagoyameshiApp.models.custom_user import CustomUser


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebhookView(View):
    def post(self, request, *args, **kwargs):
        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
            )
        except ValueError as e:
            # Invalid payload
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return HttpResponse(status=400)

        # Handle the event
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']

            # Get the user by the email stored in the checkout session
            user_email = session['customer_details']['email']
            try:
                user = CustomUser.objects.get(email=user_email)
                user.subscription = True
                user.stripe_subscription_id = session['subscription']
                user.save()
            except CustomUser.DoesNotExist:
                return HttpResponse(status=404)

        return JsonResponse({'status': 'success'}, status=200)