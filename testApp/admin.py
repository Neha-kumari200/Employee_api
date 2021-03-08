from django.contrib import admin
from .models import Company, Department, Country, Employee, Address, Degree
# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'first_name', 'middle_name', 'last_name', 'phone', 'email', 'address', 'sal', 'company', 'pan',
                    'adhar', 'country_name', 'department']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'gst', 'country']


class DepartmentAdmin(admin.ModelAdmin):
    list_filter = ['dept_name']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_line1', 'address_line2', 'address_line3', 'city', 'state', 'pin_code']


class DegreeAdmin(admin.ModelAdmin):
    list_filter = ['degree']


admin.site.register(Degree)
admin.site.register(Address, AddressAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Country)
admin.site.register(Employee, EmployeeAdmin)



