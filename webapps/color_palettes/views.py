from color_palettes.serializers import ColorPaletteSerializer
from color_palettes.models import ColorPalette
from rest_framework import viewsets


class ColorPaletteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = ColorPalette.objects.all()
    serializer_class = ColorPaletteSerializer
