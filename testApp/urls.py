from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from .views import EmployeeViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'companys', CompanyViewSet)

urlpatterns = router.urls



