from django.contrib.auth.models import User
from rest_framework import serializers
from color_palettes.models import ColorPalette


class ColorPaletteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ColorPalette
        fields = ('url', 'name', 'category_name', 'user_id', 'color_id')
