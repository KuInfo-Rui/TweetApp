from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from django.utils import timezone
import datetime


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("メールアドレスは必須です。")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("あなたには権限がありません。")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("あなたには権限がありません。")

        return self.create_user(email, password, **extra_fields)


def validate_birth_date(value):
    #未来人と、故人をNGにする
    today = datetime.date.today()
    if value > today:
        raise ValidationError("未来の日付は入力できません。")
    if value < datetime.date(1900, 1, 1):
        raise ValidationError("正しい日付を入力してください。")


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=50,
        unique=False,
        default="ユーザー名",
        verbose_name="ユーザー名",
    )

    handle = models.CharField(
        max_length=30,
        unique=True,
        #小文字のa~z,大文字のA~Z,数字の0~9,_しか使えないように設定
        validators=[RegexValidator(r'^[a-zA-Z0-9_]+$')],
        verbose_name="ハンドルネーム"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="メールアドレス",
    )

    birth_date = models.DateField(
        verbose_name="生年月日",
        null=False,
        blank=False,
        validators=[validate_birth_date],
    )

    icon = models.ImageField(
        verbose_name="ユーザーアイコン",
        upload_to="uploads",
        default='images/default_icon.png',
    )
    
    header = models.ImageField(
        verbose_name="ヘッダー画像",
        upload_to="uploads",
        default='images/default_header.jpg'
    )

    bio = models.TextField(
        verbose_name="自己紹介",
        max_length=160,
        blank=True
    )

    is_private = models.BooleanField(
        verbose_name="非公開設定",
        default=False,
    )

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=("groups"),
        blank=True,
        help_text=("The"),
        related_name="app_user_name",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific"),
        related_name="app_user_permissions",
        related_query_name="user",
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="登録日", default=timezone.now)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["handle", "birth_date"]
    objects = UserManager()

    def __str__(self):
        return self.username