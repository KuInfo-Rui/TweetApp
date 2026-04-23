from django import forms
from ..models.user import User


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "birth_date", "handle"]

    def get_initial(self):
        initial = super().get_initial()
        initial["handle"] = self.object.handle
        return initial

    username = forms.CharField(
        label="ユーザーネーム",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ユーザーネームを入力してください",
            }
        ),
    )

    birth_date = forms.DateField(
        label="生年月日",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "calendar",
            }
        ),
    )

    handle = forms.CharField(
        label="ユーザーハンドル",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "ユーザーハンドルを入力してください"}
        ),
    )
