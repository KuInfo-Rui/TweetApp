from django.db import models
from .user import User


class Tweet(models.Model):
    tweet_content = models.TextField(
        verbose_name="ツイート内容",
        max_length=140,
    )
    tweet_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tweet_by", verbose_name="投稿者"
    )
    tweet_at = models.DateTimeField(
        verbose_name="ツイート日時",
        auto_now_add=True,
    )
    parent = models.ForeignKey(
        "self",
        verbose_name="親ツイート",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
    )

    def __str__(self):
        return f"{self.tweet_by} at {self.tweet_at}"
