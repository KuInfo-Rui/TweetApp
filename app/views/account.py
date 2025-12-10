from django.shortcuts import render

def account(request, handle):
    return render(request, "app/account.html")