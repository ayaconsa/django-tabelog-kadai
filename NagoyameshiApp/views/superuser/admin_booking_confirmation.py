from django.views.generic import TemplateView



# ================== 管理者（サイト運営側）画面 ==================


# 管理者（サイト運営者）トップページ
class AdminBookingConfirmationView(TemplateView):
    template_name = "NagoyameshiApp/admin/admin_booking_confirmation.html"
