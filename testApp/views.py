from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import View
from .serializer import EmployeeSerializer


class EmployeeViewSet(viewsets.ViewSet):
    def get(self, request, *args, **kwargs):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, 200)

    def getEmployeeByCity(self, request, patna):
        queryset = Employee.objects.filter(address__city=patna)
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, 200)


