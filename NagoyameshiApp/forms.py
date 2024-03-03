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
        self.fields['name'].widget.attrs = {'placeholder': '氏名'}
        self.fields['furigana'].widget.attrs = {'placeholder': 'フリガナ'}
        self.fields['email'].widget.attrs = {'placeholder': 'メールアドレス'}
        self.fields['zipcode'].widget.attrs = {'placeholder': '郵便番号'}
        self.fields['address'].widget.attrs = {'placeholder': '住所'}
        self.fields['tel'].widget.attrs = {'placeholder': '電話番号'}
        self.fields['works'].widget.attrs = {'placeholder': 'ご職業'}
        
        
