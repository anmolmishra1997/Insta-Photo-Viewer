import datetime

from django.db import models
from django.utils import timezone


class Insta_User(models.Model):
    userid = models.BigIntegerField()
    username = models.TextField()
    full_name = models.TextField()
    profile_picture = models.TextField()
    access_token = models.TextField()

    def __str__(self):
        return self.username
