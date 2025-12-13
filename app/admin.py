from django.contrib import admin
from django.core.exceptions import FieldDoesNotExist

from .models.user import User
from .models.tweet import Tweet


def _has_field(model, name: str) -> bool:
    try:
        model._meta.get_field(name)
        return True
    except FieldDoesNotExist:
        return False


def _keep_existing(model, names):
    return [n for n in names if _has_field(model, n)]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display / list_filter は「存在するフィールドだけ」採用
    base_list_display = [
        "id",
        "display_name",
        "handle",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_display = tuple(
        name for name in base_list_display if (name in {"display_name"} or _has_field(User, name))
    )

    list_filter = tuple(_keep_existing(User, ["is_active", "is_staff", "is_superuser"]))
    search_fields = tuple(_keep_existing(User, ["username", "email", "handle"]))
    ordering = ("id",)

    # 編集画面の項目
    fieldsets = (
        (
            None,
            {"fields": tuple(_keep_existing(User, [
                "username",
                "email",
                "password",
                "handle",
                "birth_date"
            ]))},
        ),
        ("Profile", {"fields": tuple(_keep_existing(User, ["icon", "header", "bio"]))}),
        (
            "Permissions",
            {
                "fields": tuple(
                    _keep_existing(
                        User,
                        ["is_active", "is_staff", "is_superuser", "groups", "user_permissions"],
                    )
                )
            },
        ),
        ("Important dates", {"fields": tuple(_keep_existing(User, ["last_login", "date_joined"]))}),
    )

    @admin.display(description="表示名")
    def display_name(self, obj):
        # get_full_name が無いUserでも落ちないようにする
        if hasattr(obj, "get_full_name"):
            name = (obj.get_full_name() or "").strip()
            if name:
                return name

        first = (getattr(obj, "first_name", "") or "").strip()
        last = (getattr(obj, "last_name", "") or "").strip()
        full = (first + " " + last).strip()
        if full:
            return full

        return getattr(obj, "username", "") or getattr(obj, "email", "") or str(obj)


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "tweet_content", "tweet_by", "tweet_at")
    list_filter = ("tweet_at", "tweet_by")
    search_fields = ("tweet_by__username", "tweet_by__email")
    autocomplete_fields = ("tweet_by",)
    date_hierarchy = "tweet_at"
