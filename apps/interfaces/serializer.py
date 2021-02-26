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


class InterfacesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ('id', 'name')
