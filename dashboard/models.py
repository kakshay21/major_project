from django.db import models


# Create your models here.
class Equipment(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()
    priority = models.IntegerField() # higher is more important


class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    rights = models.IntegerField()  # admin - 1, noobie - 0

class Usage(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    started_at = models.DateTimeField(auto_now_add=True)
