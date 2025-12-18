from django import forms

from ..models.tweet import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["tweet_content"]

    tweet_content = forms.CharField(
        max_length=140,
        widget=forms.Textarea(
            attrs={
                "class": "input_tweet",
                "rows": 4,
                "maxlength": "140",
                "placeholder": "自由に発信してみましょう！",
            }
        ),
    )
