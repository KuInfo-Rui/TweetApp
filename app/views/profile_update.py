from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms.profileupdate_form import ProfileUpdateForm
from ..models.user import User

from django.urls import reverse_lazy


class ProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = ProfileUpdateForm
    template_name = "app/profile_setup.html"
    success_url = reverse_lazy("home")

    # ここで他人のユーザー情報を編集できないようにする。
    def get_queryset(self):
        return User.objects.filter(pk=self.request.user.pk)
