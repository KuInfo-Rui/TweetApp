from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ..forms.tweet_form import TweetForm


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.tweet_by = request.user
            tweet.save()
            return redirect("home")
    else:
        form = TweetForm()

    context = {
        "form": form,
    }
    return render(request, "app/tweet_form.html", context)
