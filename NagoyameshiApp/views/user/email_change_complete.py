from django.views.generic import TemplateView

class EmailChangeCompleteView(TemplateView):
    template_name = "NagoyameshiApp/user/email_change_complete.html"
