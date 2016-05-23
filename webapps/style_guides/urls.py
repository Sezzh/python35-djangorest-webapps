from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from style_guides.views import CategoryComponentViewSet, ComponentViewSet, StateComponentViewSet, ComponentUnitViewSet, StyleGuideViewSet

categorycomponent_list = CategoryComponentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
categorycomponent_detail = CategoryComponentViewSet.as_view({
    'get': 'retrieve'
})
component_list = ComponentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
component_detail = ComponentViewSet.as_view({
    'get': 'retrieve'
})
statecomponent_list = StateComponentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
statecomponent_detail = StateComponentViewSet.as_view({
    'get': 'retrieve'
})
componentunit_list = ComponentUnitViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
componentunit_detail = ComponentUnitViewSet.as_view({
    'get': 'retrieve'
})
styleguide_list = StyleGuideViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
styleguide_detail = StyleGuideViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    url(
        r'^categories-components/$', categorycomponent_list,
        name='categorycomponent-list'
        ),
    url(
        r'^categories-components/(?P<pk>[0-9]+)/$', categorycomponent_detail,
        name='categorycomponent-detail'
        ),
    url(
        r'^components/$', component_list,
        name='component-list'
        ),
    url(
        r'^components/(?P<pk>[0-9]+)/$', component_detail,
        name='component-detail'
        ),
    url(
        r'^states-components/$', statecomponent_list,
        name='statecomponent-list'
        ),
    url(
        r'^states-components/(?P<pk>[0-9]+)/$', statecomponent_detail,
        name='statecomponent-detail'
        ),
    url(
        r'^components-units/$', componentunit_list,
        name='componentunit-list'
        ),
    url(
        r'^components-units/(?P<pk>[0-9]+)/$', componentunit_detail,
        name='componentunit-detail'
        ),
    url(
        r'^styles-guides/$', styleguide_list,
        name='styleguide-list'
        ),
    url(
        r'^styles-guides/(?P<pk>[0-9]+)/$', styleguide_detail,
        name='styleguide-detail'
        ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
