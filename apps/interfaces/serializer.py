from rest_framework import serializers
from interfaces.models import Interfaces
from projects.models import Projects


class InterfacesModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text='项目ID')
    class Meta:
        model = Interfaces
        fields = ('id','name','tester','project','project_id','desc','create_time')
        # exclude = ('update_time', 'is_delete')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
        }

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        interface = Interfaces.objects.create(**validated_data)
        return interface

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project
        return super().update(instance, validated_data)

class InterfacesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')

class InterfacesRunSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField(help_text="环境变量ID", write_only=True)

    class Meta:
        model = Interfaces
        fields = ('id', 'env_id')