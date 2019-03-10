from django.db import models


# Create your models here.
class Equipment(models.Model):
    equip_name = models.CharField(max_length=30)
    equip_rating = models.IntegerField()