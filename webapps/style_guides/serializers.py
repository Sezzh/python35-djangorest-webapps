from django.contrib.auth.models import User
from rest_framework import serializers
from style_guides.models import CategoryComponent, Component, StateComponent, ComponentUnit, StyleGuide


class CategoryComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryComponent
        fields = ('url', 'name')


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = (
            'url', 'height', 'width', 'font_size', 'image_name', 'name',
            'description', 'rounded_comers', 'code', 'category_component_id',
            'typography_id'
            )


class StateComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StateComponent
        fields = (
            'url', 'background_color', 'font_color', 'name', 'description',
            'component_id'
            )


class ComponentUnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComponentUnit
        fields = (
            'url', 'height_unit', 'width_unit', 'font_size_unit',
            'rounded_comers_unit', 'component_id'
            )


class StyleGuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StyleGuide
        fields = (
            'url', 'project_name', 'version', 'elaboration_date',
            'default_typography', 'user_id', 'typography_id',
            'color_palette_id'
        )
