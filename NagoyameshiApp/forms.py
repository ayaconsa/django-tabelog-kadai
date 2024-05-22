from django import forms
from NagoyameshiApp.models.custom_user import CustomUser

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
        
        