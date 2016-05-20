from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from color_guide.views import UserViewSet, ColorViewSet, ColorPaletteViewSet


user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})
color_list = ColorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
color_detail = ColorViewSet.as_view({
    'get': 'retrieve'
})
colorpalette_list = ColorPaletteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
colorpalette_detail = ColorPaletteViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^colors/$', color_list, name='color-list'),
    url(r'^colors/(?P<pk>[0-9]+)/$', color_detail, name='color-detail'),
    url(r'^colors-palettes/$', colorpalette_list, name='colorpalette-list'),
    url(r'^colors-palettes/(?P<pk>[0-9]+)/$', colorpalette_detail,
        name='colorpalette-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
