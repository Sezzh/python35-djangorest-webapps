from django.db import models
from typography.models import Typography
from django.contrib.auth.models import User
from color_palettes.models import ColorPalette


# Create your models here.
class CategoryComponent(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return '%s' % (self.name)


class Component(models.Model):
    height = models.CharField(max_length=30, null=False)
    width = models.CharField(max_length=30, null=False)
    font_size = models.CharField(max_length=10, null=False)
    image_name = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=False)
    rounded_comers = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=50, null=False)
    category_component_id = models.ForeignKey(
        CategoryComponent, on_delete=models.CASCADE)
    typography_id = models.ManyToManyField(Typography)

    def __str__(self):
        return '%s' % (self.name)


class StateComponent(models.Model):
    background_color = models.CharField(max_length=30, null=False)
    font_color = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=250, null=False)
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)


class ComponentUnit(models.Model):
    height_unit = models.CharField(max_length=30, null=False)
    width_unit = models.CharField(max_length=30, null=False)
    font_size_unit = models.CharField(max_length=50, null=False)
    rounded_comers_unit = models.CharField(max_length=50, null=False)
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)


class StyleGuide(models.Model):
    project_name = models.CharField(max_length=50, null=False)
    version = models.CharField(max_length=50, null=False)
    elaboration_date = models.DateField(auto_now=False, auto_now_add=True)
    default_typography = models.CharField(max_length=50, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    typography_id = models.ManyToManyField(Typography)
    color_palette_id = models.ManyToManyField(ColorPalette)

    def __str__(self):
        return '%s' % (self.project_name)
