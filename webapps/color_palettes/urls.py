from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from color_palettes.views import ColorPaletteViewSet


colorpalette_list = ColorPaletteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
colorpalette_detail = ColorPaletteViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^colors-palettes/$', colorpalette_list, name='colorpalette-list'),
    url(r'^colors-palettes/(?P<pk>[0-9]+)/$', colorpalette_detail,
        name='colorpalette-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
