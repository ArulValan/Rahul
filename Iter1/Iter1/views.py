from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .models import *

import json
def test(request):
	return HttpResponse("Its Working")

@csrf_exempt
def login(request):
	data = request.POST
	# data=json.dumps(data)
	# data = request.body
	# data=json.dumps(request.body)
	# data = json.loads(request.body.decode('utf-8'))
	#print(data['user'])
	# p1=Person.objects.filter(user=data['user'],password=data['password'])
	#p1=Person.objects.filter(user="Vineeth",password='password')
	print(data)
	# if true:
	# print(data['name'])
	return HttpResponse("login info")

	# else:
	# 	return HttpResponse("Not logged in")
