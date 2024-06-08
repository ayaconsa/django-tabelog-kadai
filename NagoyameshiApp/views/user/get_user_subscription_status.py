from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

@require_GET
def get_user_subscription_status(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'is_authenticated': True,
            'subscription': request.user.subscription
        })
    else:
        return JsonResponse({
            'is_authenticated': False,
            'subscription': False
        })
