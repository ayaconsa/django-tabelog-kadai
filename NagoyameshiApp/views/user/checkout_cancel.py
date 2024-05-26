from django.shortcuts import render
from django.views import View

class CheckoutCancelView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'NagoyameshiApp/user/checkout_cancel.html')
