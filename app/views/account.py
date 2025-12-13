from ..models.user import User
from ..models.tweet import Tweet
from django.shortcuts import get_object_or_404, render


def account(request, handle):
    profile_user = get_object_or_404(User, handle=handle)
    viewer = request.user
    tweets = Tweet.objects.filter(tweet_by = profile_user).order_by("-tweet_at")
    context = {
        "profile_user": profile_user,
        "viewer": viewer,
        "tweets" : tweets,
    }
    return render(request, "app/account.html", context)
