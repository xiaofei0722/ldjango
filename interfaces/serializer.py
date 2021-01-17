from rest_framework import serializers
from interfaces.models import Interface
from projects.serializer import ProjectModelSerializer


class InterfaceModelSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField(slug_field='tester',queryset=)
    project = ProjectModelSerializer(label='所属项目',read_only=True)
    class Meta:
        model = Interface
        fields = "__all__"

