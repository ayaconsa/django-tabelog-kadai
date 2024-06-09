from django.views.generic import TemplateView

# お支払い方法変更（未実装）
class ChangePaymentMethodView(TemplateView):
    template_name = "NagoyameshiApp/user/change_payment_method.html"
