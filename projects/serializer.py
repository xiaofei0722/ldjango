from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from projects.models import Projects

class ProjectSerializer(serializers.Serializer):

    id = serializers.IntegerField(label='ID',read_only=True)
    name = serializers.CharField(label='项目名称', max_length=200, help_text='项目的名称',write_only=True,validators=[UniqueValidator(queryset=Projects.objects.all(),message='项目名称不能重复')])
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=50, help_text='发布应用')
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_blank=True,allow_null=True, default='简要描述')


