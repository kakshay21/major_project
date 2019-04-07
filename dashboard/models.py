from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()
    priority = models.IntegerField() # higher is more important


class UserSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rights = models.IntegerField(default=0)  # admin - 1, noobie - 0
    budget = models.IntegerField(default=0)

class Usage(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    started_at = models.DateTimeField(default=timezone.now())
    stopped_at = models.DateTimeField(default=timezone.now())
