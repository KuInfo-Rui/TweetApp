from django.views.generic import CreateView
from django.urls import reverse
from django.contrib.auth import login

from ..forms.signup_form import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "app/signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object, backend="django.contrib.auth.backends.ModelBackend")
        return response

    def get_success_url(self):
        return reverse("profile_setup", kwargs={"pk": self.object.pk})
