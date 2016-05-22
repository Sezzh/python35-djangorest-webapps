from django.contrib.auth.models import User
from colors.serializers import UserSerializer, ColorSerializer
from colors.models import Color
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
