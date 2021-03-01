from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import EnvsViewSet
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
# router.register(r'projects',views.ProjectViewSet)
#创建路由对象
# router = routers.SimpleRouter()
#注册路由
#第一个参数为prefix为路由前缀，一般添加为应用名
#第二个参数view为视图集，不要加as.view()
router.register(r'envs', EnvsViewSet)
urlpatterns = [
]
urlpatterns += router.urls