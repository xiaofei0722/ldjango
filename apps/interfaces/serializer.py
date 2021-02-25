from rest_framework import serializers
from interfaces.models import Interfaces


class InterfacesModelSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField(slug_field='tester',queryset=)
    # project = ProjectModelSerializer(label='所属项目',read_only=True)
    class Meta:
        model = Interfaces
        exclude = ('update_time', 'is_delete')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
        }


class InterfacesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')
