from rest_framework import serializers
from .models import Employee, Degree, Address, Department
from django.core.serializers import serialize

#class CompanySerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Company


'''class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ["degree"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"'''


class EmployeeSerializer(serializers.ModelSerializer):
    #degree = DegreeSerializer(many=True)
    #address = AddressSerializer(many=False)

    class Meta:
        model = Employee
        fields = "__all__"
        depth = 1

