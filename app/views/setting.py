from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def setting(request):
    return render(request, "app/setting.html")
