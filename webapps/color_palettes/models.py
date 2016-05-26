from django.db import models
from colors.models import Color
from django.contrib.auth.models import User


# Create your models here.
class ColorPalette(models.Model):
    name = models.CharField(max_length=100, null=False)
    category_name = models.CharField(max_length=100, null=False)
    user_id = models.ManyToManyField(User)
    color_id = models.ManyToManyField(Color)

    def __str__(self):
        return '%s' % (self.name)
