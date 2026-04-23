from django.contrib.auth.views import LoginView
from ..forms.login_form import TweetAppLoginForm


class TweetAppLoginView(LoginView):
    template_name = "app/login.html"
    authentication_form = TweetAppLoginForm
