from django.views.generic import TemplateView



# **************** サブスク会員のみ表示 *****************


# お支払い方法変更
class ChangePaymentMethodView(TemplateView):
    template_name = "NagoyameshiApp/change_payment_method.html"
