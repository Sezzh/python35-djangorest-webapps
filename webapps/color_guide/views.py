from django.contrib.auth.models import User
from color_guide.serializers import UserSerializer
from rest_framework import generics
from rest_framework.views import APIView


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
