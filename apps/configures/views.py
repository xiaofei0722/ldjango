import json

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from configures.models import Configures
from configures.serializer import ConfiguresModelSerializer
from interfaces.models import Interfaces
from utils import handle_datas


class ConfiguresViewSet(ModelViewSet):
    """
    list:
    获取配置信息列表数据

    create:
    创建配置信息

    destroy:
    删除配置信息

    update:
    完整更新配置信息

    partial_update:
    部分更新配置信息

    retrieve:
    获取配置信息详情数据

    """
    queryset = Configures.objects.filter(is_delete=False)
    serializer_class = ConfiguresModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ('id', 'name')

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        config_obj = self.get_object()
        config_request = json.loads(config_obj.request, encoding='utf-8')
        #处理请求头数据
        config_headers = config_request['config']['request'].get('headers')
        config_headers_list = handle_datas.handle_data4(config_headers)

        #处理全部变量数据
        config_variables = config_request['config'].get('variables')
        config_variables_list = handle_datas.handle_data2(config_variables)

        config_name = config_request['config']['name']
        selected_interface_id = config_obj.interface_id
        selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id

        datas = {
            'author': config_obj.author,
            'configure_name': config_name,
            'selected_interface_id': selected_interface_id,
            'selected_project_id': selected_project_id,
            'header': config_headers_list,
            'globalVar': config_variables_list
        }

        return Response(datas)