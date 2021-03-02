from rest_framework import serializers

from debugtalks.models import Debugtalks
from projects.models import Projects


class DebugtalksModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')
    class Meta:
        model = Debugtalks
        exclude = ('update_time', 'is_delete', 'create_time')
        read_only_fields = ('name', 'project')
        extra_kwarge = {
            'debugtalk': {
                "write_only": True
            },
        }

