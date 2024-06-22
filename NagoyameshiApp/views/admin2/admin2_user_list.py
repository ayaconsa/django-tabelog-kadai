from typing import Any
from django.views.generic import ListView
from NagoyameshiApp.models.custom_user import CustomUser
from django.shortcuts import redirect

# 管理者：会員一覧
class UserListView(ListView):
    model = CustomUser
    template_name = "NagoyameshiApp/admin2/user_list.html"

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect('login')  # ログインしていない場合、ログインページにリダイレクト
        return redirect('top')  # スタッフでない場合、トップページにリダイレクト

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sort_option = self.request.GET.get('sort', 'id') # デフォルトは会員ID順
        if sort_option == 'name':
            context['object_list'] = CustomUser.objects.all().order_by('furigana')
        elif sort_option == 'birthday':
            context['object_list'] = CustomUser.objects.all().order_by('birthday')
        elif sort_option == 'subscription':
            context['object_list'] = CustomUser.objects.all().order_by('-subscription', 'id')
        else:
            context['object_list'] = CustomUser.objects.all().order_by('id')
        context['sort_options'] = [
            ('id', '会員番号順'),
            ('name', 'フリガナ順'),
            ('birthday', '生年月日順'),
            ('subscription', 'サブスク会員')
        ]
        context['selected_sort'] = sort_option
        return context