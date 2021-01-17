from django.contrib import admin
from django.urls import path
from django.urls import include
from projects import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = DefaultRouter()
# router.register(r'projects',views.ProjectViewSet)
#创建路由对象
# router = routers.SimpleRouter()
#注册路由
#第一个参数为prefix为路由前缀，一般添加为应用名
#第二个参数view为视图集，不要加as.view()
router.register(r'xiaofei',views.ProjectViewSet)



urlpatterns = [
    # path('haha',views.haha),
    # path('',views.IndexView.as_view()),
    # path('',views.ProjectsList.as_view()),
    # path('<int:pk>/',views.ProjectsDetail.as_view())
    # path('',views.ProjectViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # }),name='projects-list'),
    # path('names/', views.ProjectViewSet.as_view({
    #     'get': 'names',
    # }), name='projects-names'),
    #
    # path('<int:pk>/',views.ProjectViewSet.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'delete':'destroy'
    # })),
    #
    # path('<int:pk>/interfaces/',views.ProjectViewSet.as_view({
    #     'get':'interfaces',
    # }))
    # path('',include(router.urls)),
]


urlpatterns += router.urls
