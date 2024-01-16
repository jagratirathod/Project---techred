from django.contrib import admin
from django.urls import path , include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from app2 import views


router = DefaultRouter()
router.register('task', views.TaskView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('app1/',include('app1.urls')),
    path('app2/',include('app1.urls')),
    path('', include(router.urls)),
]

