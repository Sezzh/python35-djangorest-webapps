from django.contrib.auth.models import User
from color_guide.serializers import UserSerializer, ColorSerializer, ColorPaletteSerializer
from color_guide.models import Color, ColorPalette
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ColorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorPaletteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer
