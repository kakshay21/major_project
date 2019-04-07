from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

import datetime

# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=30)
    rating = models.BigIntegerField()
    priority = models.IntegerField() # higher is more important
    max_mins = models.BigIntegerField(default=0) # in mins


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rights = models.IntegerField(default=0)  # admin - 1, noobie - 0
    budget = models.BigIntegerField(default=0)

class Usage(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    started_at = models.TimeField(default=datetime.datetime.now().time())
    stopped_at = models.TimeField(default=datetime.datetime.now().time())
    used_mins = models.BigIntegerField(default=0)
    percent = models.IntegerField(default=0)
