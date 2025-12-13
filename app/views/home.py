from ..models.tweet import Tweet
from django.shortcuts import render

def home(request):
    tweets = Tweet.objects.all()
    context = {
        "tweets": tweets,
    }
    return render(request, "app/home.html", context)
