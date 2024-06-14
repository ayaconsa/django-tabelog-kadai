from django import forms
from django.contrib.auth.hashers import make_password
from NagoyameshiApp.models.custom_user import CustomUser
from NagoyameshiApp.models.booking import Booking
from NagoyameshiApp.models.review import Review

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'furigana', 'email', 'birthday', 'zipcode', 'address', 'tel', 'works', 'password']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),            
            'password': forms.PasswordInput(attrs={'placeholder': 'パスワード'})
        }
        
    # CustomUserに存在しないpassword2を追記
    password2 = forms.CharField(
        label='確認用パスワード',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': '確認用パスワード'}),
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False  # メール認証のため、ユーザーを非アクティブに設定
        # パスワードをハッシュ化
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields['name'].widget.attrs = {'placeholder': '侍 太郎'}
        self.fields['furigana'].widget.attrs = {'placeholder': 'サムライ タロウ'}
        self.fields['email'].widget.attrs = {'placeholder': 'taro.samurai@example.com'}
        self.fields['zipcode'].widget.attrs = {'placeholder': '123-1234'}
        self.fields['address'].widget.attrs = {'placeholder': '東京都千代田区'}
        self.fields['tel'].widget.attrs = {'placeholder': '09012345678'}
        self.fields['works'].widget.attrs = {'placeholder': 'エンジニア'}
        
class EmailChangeForm(forms.Form):
    new_email = forms.EmailField(label='新しいメールアドレス', required=True, widget=forms.EmailInput(attrs={'placeholder': 'taro.samurai@example.com'}))


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'number_of_persons']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.Select(choices=Booking.TIME_Sorted),
            'number_of_persons': forms.NumberInput(attrs={'min': 1, 'max': 12}),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['score', 'comment']
        widgets = {
            'score': forms.RadioSelect,
        }