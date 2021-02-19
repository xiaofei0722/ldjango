from django.contrib import admin
from django.urls import path
from django.urls import include
from interfaces import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'projects',views.ProjectViewSet)
urlpatterns = [
    # path('haha',views.haha),
    # path('',views.IndexView.as_view()),
    path('',views.InterfaceList.as_view()),
    path('<int:pk>/',views.InterfaceDetail.as_view())
]

# urlpatterns += router.urls
