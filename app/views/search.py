from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..models.tweet import Tweet


@login_required
def search(request):
    query = request.GET.get("query")
    if query:
        result = Tweet.objects.filter(tweet_content__icontains=query)
        context = {
            "result": result,
            "query": query,
        }
        return render(request, "app/search.html", context)
    else:
        return render(request, "app/search.html")
