from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

# Create your views here.

def employee(request):
	if request.method == "GET":
		employee = Employee.objects.all().values()
		template = loader.get_template('employee.html')
		context = {'employee':employee,
		}
		return HttpResponse(template.render(context, request))

	if request.method == "POST":
		data = request.POST
		return data