from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='确认密码',
                                             min_length=6,
                                             max_length=20,
                                             write_only=True,
                                             help_text='确认密码',
                                             error_messages={'min_length': '只允许6-20个字符的确认密码',
                                                             'max_length': '只允许6-20个字符的确认密码'})
    token = serializers.CharField(label='生成token',
                                  read_only=True,)


    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'email', 'password_confirm', 'token')
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {'min_length': '只允许6-20个字符的用户名',
                                   'max_length': '只允许6-20个字符的用户名'}
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                #添加邮箱重复效验
                'validators': [UniqueValidator(queryset=User.objects.all(), message="此邮箱已注册")]
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {'min_length': '只允许6-20个字符的用户名',
                                   'max_length': '只允许6-20个字符的用户名'}
            },
        }
    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('两次输入密码不相同')
        return attrs

    def create(self, validated_data):
        #移除数据库模型类中不存在的属性
        validated_data.pop('password_confirm')
        #保存数据
        user = User.objects.create_user(**validated_data)

        #创建手动创建token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user