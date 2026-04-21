from django import forms
from django.contrib.auth.forms import AuthenticationForm


class TweetAppLoginForm(AuthenticationForm):
    """
    models.user.pyにてUSERNAME_FIELDにemailを指定しているため
    email入力欄が変数名はusernameとなっていることに注意
    """

    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "メールアドレスを入力してください",
            }
        )
    )

    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "パスワードを入力してください",
            }
        ),
    )
