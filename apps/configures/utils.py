import re
from django.db.models import Count
from rest_framework import serializers

from interfaces.models import Interfaces
from projects.models import Projects
from testsuits.models import Testsuits
def whether_existed_project_id(value):
    if not isinstance(value, int):
        raise serializers.ValidationError('所选项目有误')
    elif not Projects.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError('所选项目不存在')

def whether_existed_interface_id(value):
    if not isinstance(value, int):
        raise serializers.ValidationError('所选接口有误')
    elif not Projects.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError('所选接口不存在')