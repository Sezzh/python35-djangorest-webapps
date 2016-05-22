from django.db import models
from colors.models import Color
from django.contrib.auth.models import User


# Create your models here.
class ColorPalette(models.Model):
    color = models.ManyToManyField(Color)
    name = models.CharField(max_length=100, null=False)
    category_name = models.CharField(max_length=100, null=False)
    user = models.ManyToManyField(User)
