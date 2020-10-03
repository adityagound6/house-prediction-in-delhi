from django.db import models


# Create your models here.

class Predicted(models.Model):
    area = models.FloatField()
    location = models.IntegerField()
    bhk = models.IntegerField()
    boathroom = models.IntegerField()
