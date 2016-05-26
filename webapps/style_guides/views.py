from django.contrib.auth.models import User
from rest_framework import viewsets
from style_guides.serializers import CategoryComponentSerializer, ComponentSerializer, StateComponentSerializer, ComponentUnitSerializer, StyleGuideSerializer
from style_guides.models import CategoryComponent, Component, StateComponent, ComponentUnit, StyleGuide


class CategoryComponentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CategoryComponent.objects.all()
    serializer_class = CategoryComponentSerializer


class ComponentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer


class StateComponentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = StateComponent.objects.all()
    serializer_class = StateComponentSerializer


class ComponentUnitViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ComponentUnit.objects.all()
    serializer_class = ComponentUnitSerializer


class StyleGuideViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = StyleGuide.objects.all()
    serializer_class = StyleGuideSerializer
