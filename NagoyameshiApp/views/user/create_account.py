from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from ...forms import UserCreateForm

# ================== ユーザー画面 ==================
# ************** 非会員でも表示できる画面 **************

# アカウントの新規登録
class CreateAccountView(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get("username")
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/")
        return render(request, "NagoyameshiApp/account_create.html", {"form": form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, "NagoyameshiApp/account_create.html", {"form": form,})

create_account = CreateAccountView.as_view()
