"""ldjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='肖飞API接口文档平台',
        default_version='v1',
        description='这是一个牛逼的接口文档',
        contact=openapi.Contact(email='282825724@qq.com'),
        license=openapi.License(name='BSD License')

    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('projects.urls')),
    path('',include('interfaces.urls')),
    path('',include('envs.urls')),
    path('',include('debugtalks.urls')),
    path('',include('testsuits.urls')),
    path('',include('reports.urls')),

    # path('api/',include('rest_framework.urls'))
    path('docs/',include_docs_urls(title='测试平台接口文档',
                                   description='这是一个牛逼的接口文档平台')),

    # re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    #         schema_view.without_ui(cache_timeout=0),name='schema-json'),
    # path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    # path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc-ui'),
    path('api/',include('rest_framework.urls')),

    path('user/',include('user.urls')),
]
