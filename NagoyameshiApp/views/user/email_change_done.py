from django.views.generic import TemplateView

class EmailChangeDoneView(TemplateView):
    template_name = "NagoyameshiApp/user/email_change_done.html"