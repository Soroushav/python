from django.db import models
from django_comments.moderation import CommentModerator, moderator


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    enable_comment = models.BooleanField(default=True)

class Comment(CommentModerator):
    enable_field = 'enable_comment'

moderator.register(Food, Comment)