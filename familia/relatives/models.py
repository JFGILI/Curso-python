from django.db import models

class Relatives(models.Model):
    name = models.CharField(max_length=50)
    birth = models.IntegerField()
    alive = models.BooleanField()
