from django.contrib import admin
from django.urls import path
from django.urls import include
from projects import views
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'projects',views.ProjectViewSet)
urlpatterns = [
    # path('haha',views.haha),
    # path('',views.IndexView.as_view()),
    path('',views.ProjectsList.as_view()),
    path('<int:pk>/',views.ProjectsDetail.as_view())
]

# urlpatterns += router.urls
