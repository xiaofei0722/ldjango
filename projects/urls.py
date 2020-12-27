from django.contrib import admin
from django.urls import path
from django.urls import include
from projects import views

urlpatterns = [
    # path('haha',views.haha),
    path('',views.IndexView.as_view()),
    path('<int:pk>/',views.IndexView.as_view())
]
