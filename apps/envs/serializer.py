from rest_framework import serializers

from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects


class EnvsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        exclude = ('update_time', 'is_delete')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
        }

#     def create(self, validated_data):validated_data
#         project = validated_data.pop('project_id')
#         validated_data['project'] = project
#         interface = Interfaces.objects.create(**validated_data)
#         return interface
#
#     def update(self, instance, validated_data):
#         if 'project_id' in validated_data:
#             project = validated_data.pop('project_id')
#             validated_data['project'] = project
#         return super().update(instance, validated_data)
#
class EnvsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ('id', 'name')
