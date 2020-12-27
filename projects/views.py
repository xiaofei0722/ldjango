import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


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
    def get(self,request,pk):
        data = {
            'name': 'xiaofei',
            "age": 17
        }
        dataj = json.dumps(data)
        # return JsonResponse(content=data)

        return HttpResponse(content=dataj,content_type='application/json', status=222)
        # return HttpResponse('这是一个get请求,pk是'+str(pk))
        # return render(request, 'demo.html')
    def post(self,request):
        return HttpResponse('这是一个Post请求')

    def put(self,request):
        return HttpResponse('这是一个Put请求')

    def delete(self,request):
        return HttpResponse('这是一个delete请求')