from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def employee(request):
	if request.method == "GET":
		employee = Employee.objects.all().values()
		template = loader.get_template('employee.html')
		context = {'employee':employee,
			 }
		return HttpResponse(template.render(context, request))

#	elif request.method == "POST":
#		data = json.loads(request.POST)
#		print(request)
#		return HttpResponse(data.get("firstname"))