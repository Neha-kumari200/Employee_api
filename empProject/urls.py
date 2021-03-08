"""empProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
print("urls.py")
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from testApp import viewsfromimportfrom

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/employee/', views.EmployeeViewSet.as_view({'get': 'get'})),
    path('api/v1/employee/<str:patna>', views.EmployeeViewSet.as_view({'get': 'getEmployeeByCity'})),

    #path('', include('testApp.urls')),
    #path('api/', include('testApp.urls')),

]
urlpatterns = format_suffix_patterns(urlpatterns)