from django.db import models
from django.core import validators
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=30, unique=True)
    gst = models.IntegerField(unique=True)
    country = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company Table"
        db_table = "Company"

    def __str__(self):
        return self.name


class Department(models.Model):
    dept_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments Table"
        db_table = "Department"

    def __str__(self):
        return self.dept_name


class Country(models.Model):
    country_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countrys Table"
        db_table = "Country"


    def __str__(self):
        return self.country_name


class Address(models.Model):
    address_line1 = models.TextField(max_length=30)
    address_line2 = models.TextField(max_length=30)
    address_line3 = models.TextField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    pin_code = models.IntegerField()

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses Table"
        db_table = "Address"

    def __str__(self):
        return self.city


class Degree(models.Model):
    degree = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Degree"
        verbose_name_plural = "Degrees Table"
        db_table = "Degree"

    def __str__(self):
        return self.degree


class Employee(models.Model):
    eno = models.IntegerField(null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField(unique=True, null=False, blank=False)
    email = models.EmailField(validators=[validators.EmailValidator], unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    sal = models.IntegerField()
    company = models.ForeignKey(Company, related_name='Employee', on_delete=models.CASCADE)
    pan = models.CharField(max_length=10, unique=True)
    adhar = models.IntegerField(unique=True)
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE)
    degree = models.ManyToManyField(Degree)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees Table"
        db_table = "Employee"

    def __int__(self):
        return self.eno
