from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from NagoyameshiApp.models.custom_user import CustomUser
import stripe

# 支払い成功（会員のみ）
class CheckoutSuccessView(View):
    def get(self, request, *args, **kwargs):    
        session_id = request.GET.get('session_id')
        user_id = request.GET.get('user_id')

        if not session_id or not user_id:
            return HttpResponse("Invalid request", status=400)
        
        # ここで、session_idを使って支払いが成功したかどうかを確認することもできます
        # 例:
        # session = stripe.checkout.Session.retrieve(session_id)
        # if session.payment_status != 'paid':
        #     return HttpResponse("Payment not completed", status=400)

        # ユーザーの subscription 項目を更新
        user = get_object_or_404(CustomUser, id=user_id)
        user.subscription = True
        user.save()

        return render(request, 'NagoyameshiApp/user/checkout_success.html')