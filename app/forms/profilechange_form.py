from django import forms

from ..models.user import User


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "handle", "header", "icon", "bio"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "handle": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "header": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",  # 画像ファイルであるかどうかをバリデーション
                }
            ),
            "icon": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                }
            ),
        }
