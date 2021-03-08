# Generated by Django 2.2.7 on 2020-01-12 09:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.TextField(max_length=30)),
                ('address_line2', models.TextField(max_length=30)),
                ('address_line3', models.TextField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('pin_code', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'db_table': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('gst', models.IntegerField(unique=True)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companys',
                'db_table': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': ('Countrys',),
                'db_table': 'Country',
            },
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Degree',
                'verbose_name_plural': 'Degrees',
                'db_table': 'Degree',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'db_table': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator])),
                ('sal', models.IntegerField()),
                ('pan', models.CharField(max_length=10, unique=True)),
                ('adhar', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(12)])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.Address')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employee', to='testApp.Company')),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.Country')),
                ('degree', models.ManyToManyField(to='testApp.Degree')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.Department')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
                'db_table': 'Employee',
            },
        ),
    ]
