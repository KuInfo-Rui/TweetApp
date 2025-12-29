from django.shortcuts import render
from forms.tweet_form import TweetForm

def tweet_create_view(request):
    form = TweetForm
    context = {
        form : "form",
    }
    render(request, "app/tweet_form.html", context)