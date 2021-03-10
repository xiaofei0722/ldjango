from rest_framework import serializers
from interfaces.models import Interfaces
from projects.models import Projects
from testsuits.models import Testsuits


class TestSuitsModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')
    project_id = serializers.PrimaryKeyRelatedField(queryset=Projects.objects.all(), help_text='项目ID')
    class Meta:
        model = Testsuits
        fields = ('id','name','project','project_id','create_time','update_time','include')
        # exclude = ('update_time', 'is_delete')
        extra_kwarge = {
            'create_time': {
                "read_only": True
            },
        }

    def create(self, validated_data):
        project = validated_data.pop('project_id')
        validated_data['project'] = project
        testsuit = Testsuits.objects.create(**validated_data)
        return testsuit

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop('project_id')
            validated_data['project'] = project
        return super().update(instance, validated_data)

class TestSuitsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testsuits
        fields = ('id', 'name')

class TestsuitsRunSerializer(serializers.ModelSerializer):
    env_id = serializers.IntegerField(help_text="环境变量ID", write_only=True)

    class Meta:
        model = Testsuits
        fields = ('id', 'env_id')