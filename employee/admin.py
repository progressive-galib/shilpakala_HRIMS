from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeList(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)

admin.site.register(Employee, EmployeeList)