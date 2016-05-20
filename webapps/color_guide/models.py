from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Color(models.Model):
    user = models.ManyToManyField(User)
    hexa = models.CharField(max_length=15, null=False)
    opacity = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    rgb = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=100, null=False)
