import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views import View

from interfaces.models import Interface
from projects.models import Projects

# def haha(request):
#     if request.method == 'GET':
#
#         haha = '这是一个get请求'
#
#         return HttpResponse(haha)
#     if request.method == 'POST':
#
#         return HttpResponse('这是一个Post请求')
#     else:
#         return HttpResponse('这是一个其他请求')


class IndexView(View):
    def get(self,request):
        # one_obj = Projects(name='这是一个牛逼的项目',leader='leo',programer='xixi',publish_app='这是一个厉害的应用',desc='没有描述')
        # one_obj.save()
        # Projects.objects.create(name='这是一个好玩的项目',leader='aaa',programer='bbb',publish_app='这是一个好玩的应用',tester='xf',desc='没有描述')
        # a = Projects.objects.all()
        # one_obj = Projects.objects.get(id=1).leader
        # one_obj = Projects.objects.filter(desc__contains='简要')

        # one_obj = Projects.objects.filter(interface__name='登录接口')
        # one_obj = Interface.objects.filter(project__name='接口自动化')

        # one_obj = Projects.objects.filter(id__gt=2)

        # one_obj = Projects.objects.filter(id=2,leader='张三')
        # one_obj = Projects.objects.filter(Q(id=2)| Q(leader='leo'))

        # one_obj = Projects.objects.filter(desc__contains='描述')
        # one_obj = one_obj.filter(leader='leo').first().desc

        # one_obj = Projects.objects.get(id=1)
        # one_obj.leader='肖飞大神'
        # one_obj.save()

        # one_obj =Projects.objects.filter(name__contains='1')
        # one_obj1 = one_obj.first()
        # one_obj1.delete()

        one_obj = Projects.objects.filter(id__gte=1).order_by('programer')

        return HttpResponse(one_obj)
        # return HttpResponse('这是一个get请求,pk是'+str(pk))
        # return render(request, 'demo.html')
    def post(self,request):
        return HttpResponse('这是一个Post请求')

    def put(self,request):
        return HttpResponse('这是一个Put请求')

    def delete(self,request):
        return HttpResponse('这是一个delete请求')