from django.shortcuts import render


def top(request):
    return render(request, "app/top.html")
