from django.shortcuts import render

def setting(request):
    return render(request, "app/setting.html")