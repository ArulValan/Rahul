from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from .models import *

import json
def test(request):
	return HttpResponse("Its Working")

@csrf_exempt
def login(request):
	data = json.loads(request.POST)
	#print(data['user'])
	p1=Person.objects.filter(user=data['user'],password=data['password'])
	#p1=Person.objects.filter(user="Vineeth",password='password')
	print(data)
	if p1:
		
		return HttpResponse("login info")
		print("Logged in")
	else:
		return HttpResponse("Not logged in")
		print("Not Logged in")
