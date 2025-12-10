from django.shortcuts import render

def notice(request):
    return render(request, "app/notice.html")