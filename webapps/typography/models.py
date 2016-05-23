from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Typography(models.Model):
    name = models.CharField(max_length=50, null=False)
    file_name = models.CharField(max_length=50, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)
