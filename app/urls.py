from django.urls import path
from app.views import(
    account,
    home,
    message,
    notice,
    search,
    setting,
)

urlpatterns = [
    path("home/", home, name="home"),
    path("search/", search, name="search"),
    path("notice/", notice, name="notice"),
    path("message/", message, name="message"),
    path("setting/", setting, name="setting"),
    path("account/<str:handle>/", account, name="account"),
]
