from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

class PasswordChangeDoneView(LoginRequiredMixin, TemplateView):
    template_name = 'NagoyameshiApp/user/password_change_done.html'