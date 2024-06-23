from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.forms import AccountInfoEditForm

# 会員情報編集（会員のみ）
class AccountInfoEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = AccountInfoEditForm
    template_name = "NagoyameshiApp/user/account_info_update.html"
    success_url = '/account_info/'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        for v in form.fields.values():
            v.label_suffix = ""
        return context
