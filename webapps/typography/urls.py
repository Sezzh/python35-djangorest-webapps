from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from typography.views import TypographyViewSet


typography_list = TypographyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
typography_detail = TypographyViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    url(r'^typographys/$', typography_list, name='typography-list'),
    url(r'^typographys/(?P<pk>[0-9]+)/$', typography_detail,
        name='typography-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
