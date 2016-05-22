from rest_framework import serializers
from typography.models import Typography


class TypographySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Typography
        fields = ('url', 'name', 'file_name', 'user')
