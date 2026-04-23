from django.urls import path

from app.views.login import TweetAppLoginView
from app.views.sign_up import SignUpView
from app.views.profile_update import ProfileUpdateView

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
    path("login/", TweetAppLoginView.as_view(), name="login"),
    path("top/", top, name="top"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile_setup/<int:pk>/", ProfileUpdateView.as_view(), name="profile_setup"),
]
