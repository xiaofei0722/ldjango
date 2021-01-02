import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from django.views import View
import json
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


# class IndexView(View):
#     def get(self,request):
#         # one_obj = Projects(name='这是一个牛逼的项目',leader='leo',programer='xixi',publish_app='这是一个厉害的应用',desc='没有描述')
#         # one_obj.save()
#         # Projects.objects.create(name='这是一个好玩的项目',leader='aaa',programer='bbb',publish_app='这是一个好玩的应用',tester='xf',desc='没有描述')
#         # a = Projects.objects.all()
#         # one_obj = Projects.objects.get(id=1).leader
#         # one_obj = Projects.objects.filter(desc__contains='简要')
#
#         # one_obj = Projects.objects.filter(interface__name='登录接口')
#         # one_obj = Interface.objects.filter(project__name='接口自动化')
#
#         # one_obj = Projects.objects.filter(id__gt=2)
#
#         # one_obj = Projects.objects.filter(id=2,leader='张三')
#         # one_obj = Projects.objects.filter(Q(id=2)| Q(leader='leo'))
#
#         # one_obj = Projects.objects.filter(desc__contains='描述')
#         # one_obj = one_obj.filter(leader='leo').first().desc
#
#         # one_obj = Projects.objects.get(id=1)
#         # one_obj.leader='肖飞大神'
#         # one_obj.save()
#
#         # one_obj =Projects.objects.filter(name__contains='1')
#         # one_obj1 = one_obj.first()
#         # one_obj1.delete()
#
#         one_obj = Projects.objects.filter(id__gte=1).order_by('programer')
#
#         return HttpResponse(one_obj)
#         # return HttpResponse('这是一个get请求,pk是'+str(pk))
#         # return render(request, 'demo.html')
#     def post(self,request):
#         return HttpResponse('这是一个Post请求')
#
#     def put(self,request):
#         return HttpResponse('这是一个Put请求')
#
#     def delete(self,request):
#         return HttpResponse('这是一个delete请求')


class ProjectsList(View):

    def get(self,request):

        project_qs = Projects.objects.all()

        project_list = []

        for project in project_qs:

            one_dict = {
                'name':project.name,
                'leader':project.leader,
                'tester':project.tester,
                'programer':project.programer,
                'publish_app':project.publish_app,
                'desc':project.desc
            }

            project_list.append(one_dict)

        return JsonResponse(project_list,safe=False)

    def post(self,request):

        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data,encoding='utf-8')

        # new_project = Projects.objects.create(name=python_data['name'],
        #                         leader=python_data['leader'],
        #                         tester=python_data['tester'],
        #                         programer=python_data['programer'],
        #                         publish_app=python_data['publish_app'],
        #                         desc=python_data['desc'])

        project = Projects.objects.create(**python_data)


        one_dict = {
            'name':project.name,
            'leader':project.leader,
            'tester':project.tester,
            'programer':project.programer,
            'publish_app':project.publish_app,
            'desc':project.desc
        }



        return JsonResponse(one_dict)

class ProjectsDetail(View):

    def get(self,request,pk):

        project = Projects.objects.get(id=pk)

        one_dict = {
            'name': project.name,
            'leader': project.leader,
            'tester': project.tester,
            'programer': project.programer,
            'publish_app': project.publish_app,
            'desc': project.desc
        }

        return JsonResponse(one_dict)

    def put(self,request,pk):

        project = Projects.objects.get(id=pk)

        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')

        project.name = python_data['name']
        project.leader = python_data['leader']
        project.tester = python_data['tester']
        project.programer = python_data['programer']
        project.publish_app = python_data['publish_app']
        project.desc = python_data['desc']
        project.save()

        one_dict = {
            'name': project.name,
            'leader': project.leader,
            'tester': project.tester,
            'programer': project.programer,
            'publish_app': project.publish_app,
            'desc': project.desc
        }

        return JsonResponse(one_dict,status=201)


    def delete(self,request,pk):
        project = Projects.objects.get(id=pk)
        project.delete()
        return JsonResponse(None,safe=False,status=204)