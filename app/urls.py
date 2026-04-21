from django.urls import path

from django.contrib.auth import views as auth_views
from .forms.login_form import TweetAppLoginForm

from app.views import (
    account,
    home,
    message,
    notice,
    search,
    setting,
    tweet_create,
    top,
)

urlpatterns = [
    path("home/", home, name="home"),
    path("search/", search, name="search"),
    path("notice/", notice, name="notice"),
    path("message/", message, name="message"),
    path("setting/", setting, name="setting"),
    path("account/<str:handle>/", account, name="account"),
    path("tweet_form/", tweet_create, name="tweet_form"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="app/login.html",
            authentication_form=TweetAppLoginForm,
        ),
        name="login",
    ),
    path("top/", top, name="top"),
]
