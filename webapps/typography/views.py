from typography.serializers import TypographySerializer
from typography.models import Typography
from rest_framework import viewsets


class TypographyViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Typography.objects.all()
    serializer_class = TypographySerializer


class ColorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Typography.objects.all()
    serializer_class = TypographySerializer
