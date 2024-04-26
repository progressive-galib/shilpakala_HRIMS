from django.contrib import admin
from .models import Employee, Leave, ACR

# Register your models here.
class EmployeeList(admin.ModelAdmin):
  list_display = ("firstname", "lastname",)

admin.site.register(Employee, EmployeeList)
admin.site.register(Leave)
admin.site.register(ACR)