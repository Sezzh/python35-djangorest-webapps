from django.contrib.auth.models import User
from color_guide.serializers import UserSerializer, ColorSerializer
from rest_framework import generics
from rest_framework.views import APIView
from color_guide.models import Color
from rest_framework import viewsets
from rest_framework.decorators import detail_route

"""
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorDetail(generics.RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
"""


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
