from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from configures.models import Configures
from debugtalks.models import Debugtalks
from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects
from reports.models import Reports
from testcases.models import Testcases
from testsuits.models import Testsuits


class SummaryAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        '''
        获取统计信息
        :param request:
        :return:
        '''
        user = request.user
        user_info = {
            'username': user.username,
            'role': '管理员' if user.is_superuser else '普通用户',
            'date_jojined': user.date_joined.strftime('%Y-%m-%d %H:%M:%S') if user.date_joined else '',
            'last_login': user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else '',
        }

        projects_count = Projects.objects.filter(is_delete=False).count()
        interfaces_count = Interfaces.objects.filter(is_delete=False).count()
        testcases_count = Testcases.objects.filter(is_delete=False).count()
        testsuits_count = Testsuits.objects.filter(is_delete=False).count()
        configures_count = Configures.objects.filter(is_delete=False).count()
        envs_count = Envs.objects.filter(is_delete=False).count()
        debug_talks_count = Debugtalks.objects.filter(is_delete=False).count()
        reports_count = Reports.objects.filter(is_delete=False).count()

        run_testcases_success_count = Reports.objects.filter(is_delete=False).aggregate(Sum('success'))['success__sum'] or 0
        run_testcases_total_count = Reports.objects.filter(is_delete=False).aggregate(Sum('count'))['count__sum'] or 0

        if run_testcases_total_count:
            success_rate = int((run_testcases_success_count / run_testcases_total_count) *100 )
            fail_rate = 100 - success_rate
        else:
            success_rate = 0
            fail_rate = 0

        statistice = {
            'projects_count': projects_count,
            'interfaces_count': interfaces_count,
            'testcases_count': testcases_count,
            'testsuits_count': testsuits_count,
            'configures_count': configures_count,
            'envs_count': envs_count,
            'debug_talks_count': debug_talks_count,
            'reports_count': reports_count,
            'success_rate': success_rate,
            'fail_rate': fail_rate
        }
        return Response(data={
            'user': user_info,
            'statistics': statistice
        })
