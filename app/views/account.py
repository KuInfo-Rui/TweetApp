from ..models.user import User
from django.shortcuts import get_object_or_404, render


def account(request, handle):
    profile_user = get_object_or_404(User, handle=handle)
    viewer = request.user
    context = {
        "profile_user": profile_user,
        "viewer": viewer,
    }
    return render(request, "app/account.html", context)
