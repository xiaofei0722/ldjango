from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from projects.models import Projects

def is_unique_porject_name(name):
    if '项目' not in name:
        raise serializers.ValidationError(detail='项目名称中必须包含"项目"')

class ProjectSerializer(serializers.Serializer):

    id = serializers.IntegerField(label='ID',read_only=True)
    name = serializers.CharField(label='项目名称', max_length=200, help_text='项目的名称',write_only=True,validators=[UniqueValidator(queryset=Projects.objects.all(),message='项目名称不能重复'),is_unique_porject_name],
                                 error_messages={'max_length':'长度不能超过200个字节',
                                                 'min_length':'长度不能超过6个字节'})
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=50, help_text='发布应用')
    desc = serializers.CharField(label='简要描述', help_text='简要描述', allow_blank=True,allow_null=True, default='简要描述')
    def validate_name(self,value):
        if not value.endswith('项目'):
            raise serializers.ValidationError(detail='项目名称必须以"项目"结尾')
        return value

    def validate(self, attrs):
        if '飞' not in attrs['tester'] and '飞' not in attrs['leader']:
            raise serializers.ValidationError('负责人或者测试人员必须名字带飞')
        return attrs

    def create(self, validated_data):
        prject = Projects.objects.create(**validated_data)
        return prject

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.leader = validated_data['leader']
        instance.tester = validated_data['tester']
        instance.programer = validated_data['programer']
        instance.publish_app = validated_data['publish_app']
        instance.desc = validated_data['desc']
        instance.save()
        return instance

class ProjectModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='项目名称', max_length=200,min_length=2, help_text='项目的名称', #write_only=True,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(), message='项目名称不能重复'),
                                             is_unique_porject_name])
    class Meta:
        model = Projects
        fields = "__all__"
        # fields = ('id','name','leader','tester','programer')
        # exclude = ('publish_app', 'desc')
        # read_only_fields = ('leader','test')
        # extra_kwargs = {
        #     'leader':{
        #         'write_only': True,
        #         'error_messages':{'max_length':'长度不能超过200个字节','min_length':'长度不能少于6个字节'}
        #     }
        #
        # }
    # def validate_name(self,value):
    #     if not value.endswith('项目'):
    #         raise serializers.ValidationError(detail='项目名称必须以"项目"结尾')
    #     return value

    # def validate(self, attrs):
    #     if '飞' not in attrs['tester'] and '飞' not in attrs['leader']:
    #         raise serializers.ValidationError('负责人或者测试人员必须名字带飞')
    #     return attrs