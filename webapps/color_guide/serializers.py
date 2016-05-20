from django.contrib.auth.models import User
from rest_framework import serializers
from color_guide.models import Color, ColorPalette


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'last_name', 'first_name')


class ColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Color
        fields = ('url', 'hexa', 'opacity', 'rgb', 'name', 'user')


class ColorPaletteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ColorPalette
        fields = ('url', 'name', 'category_name', 'color')
