import os
from datetime import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from envs.models import Envs
from ldjango import settings
from testcases.models import Testcases
from testsuits.models import Testsuits
from testsuits.serializer import TestSuitsModelSerializer, TestSuitsNameSerializer, TestsuitsRunSerializer
from testsuits.utils import handle_testsuit, get_testcases_by_interface_ids
from utils import common


class TestSuitsViewSet(viewsets.ModelViewSet):
    """
    list:
    获取套件列表数据

    create:
    创建套件

    destroy:
    删除套件

    update:
    完整更新套件

    partial_update:
    部分更新套件

    retrieve:
    获取套件详情数据

    names:
    获取所有套件ID和接口名


    """
    queryset = Testsuits.objects.filter(is_delete=False)
    serializer_class = TestSuitsModelSerializer
    filter_fields = ['id', 'name']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()  # 逻辑删除

    def list(self, request, *args, **kwargs):
        #过滤查询集的创建
        # queryset = self.filter_queryset(self.get_queryset())
        # #分页查询集的创建
        # page = self.paginate_queryset(queryset)
        # #如果要分页就把分页信息以及分页后处理的逻辑返回
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     datas = serializer.data
        #     datas = get_count_by_interface(datas)
        #     return self.get_paginated_response(datas)
        # #如果不分页就直接返回查询集信息
        # serializer = self.get_serializer(queryset, many=True)
        # datas = serializer.data
        # datas = get_count_by_interface(datas)
        # return Response(datas)
        response = super().list(request,*args,**kwargs)
        response.data['results'] = handle_testsuit(response.data['results'])
        return response

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TestSuitsNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def run(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid()
        datas = serializer.validated_data

        env_id = datas.get('env_id')
        testcase_dir_path = os.path.join(settings.SUITES_DIR, datetime.strftime(datetime.now(), '%Y%m%d%H%M%S%f'))
        if not os.path.exists(testcase_dir_path):
            os.mkdir(testcase_dir_path)

        # first()返回queryset查询集第一项
        env = Envs.objects.filter(id=env_id, is_delete=False).first()

        include = eval(instance.include)

        if len(include) == 0:
            data_dict = {
                'detail': '此套件下未添加用例，无法运行'
            }
            return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

        # 将include中的接口id转换为此接口下的id
        include = get_testcases_by_interface_ids(include)

        for testcase_id in include:
            testcase_objs = Testcases.objects.filter(is_delete=False, id=testcase_id).first()

            if testcase_objs:
                # 生成yml文件
                common.generate_testcase_files(testcase_objs, env, testcase_dir_path)

        # 运行用例
        return common.run_testcase(instance, testcase_dir_path)

    def get_serializer_class(self):
        return TestsuitsRunSerializer if self.action == 'run' else self.serializer_class