from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models.user import User

import string
import random


def handle_generate():
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=12))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        # UserCreationFormはパスワード入力欄を自動で作ってくれる
        fields = ["email"]

    email = forms.EmailField(
        label="メールアドレス",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "メールアドレスを入力してください",
            }
        ),
    )

    password1 = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "パスワードを入力してください",
            }
        ),
    )

    password2 = forms.CharField(
        label="パスワード(確認用)",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "もう一度入力してください",
            }
        ),
    )

    # commitがややこしいことに注意。
    # 基本的にはcommitがTrueなら保存、commitがFalseならユーザー名と生年月日を補うメソッド
    # ただ基本的にはcommitがTrueの状態でviewsは呼び出すためifを通過すると思っていい。
    # 関数の中で関数が呼び出されて、補う→保存を一気に行う。
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = "ユーザー名"
        user.birth_date = "2001-01-01"
        # 万が一ハンドルが被らないためにwhileループを利用
        while True:
            new_handle = handle_generate()
            if not User.objects.filter(handle=new_handle).exists():
                user.handle = new_handle
                break

        if commit:
            user.save()
        return user
