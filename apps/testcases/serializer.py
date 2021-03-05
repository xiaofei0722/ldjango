from rest_framework import serializers

from configures.utils import whether_existed_project_id, whether_existed_interface_id
from interfaces.models import Interfaces
from projects.models import Projects
from configures.models import Configures
from testcases.models import Testcases


class InterfacesAnotherSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')
    #项目id
    pid = serializers.IntegerField(write_only=True, validators=[whether_existed_project_id], help_text='项目id')
    # 接口id
    iid = serializers.IntegerField(write_only=True, validators=[whether_existed_interface_id], help_text='接口id')
    class Meta:
        model = Interfaces
        fields = ('iid', 'name', 'project', 'pid')
        extra_kwargs = {
            'name': {
                'read_only': True  # 只输出
            }
        }
    def validate(self, attrs):
        if not Interfaces.objects.filter(id=attrs['iid'], project_id=attrs['pid'], is_delete=False).exists():
            raise serializers.ValidationError('项目和接口信息不对应')
        return attrs

class TestcasesModelSerializer(serializers.ModelSerializer):
    interface = InterfacesAnotherSerializer(help_text='所属接口和项目信息')
    class Meta:
        model = Testcases
        fields = ('id','name','interface','include','author','request')
        # exclude = ('update_time', 'is_delete')
        extra_kwarge = {
            'request': {
                "write_only": True
            },
            'include': {
                "write_only": True
            },
        }

    def create(self, validated_data):
        interface_dict = validated_data.pop('interface')
        validated_data['interface_id'] = interface_dict['iid']
        return Testcases.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return super().update(instance, validated_data)

