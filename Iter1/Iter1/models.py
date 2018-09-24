from django.db import models

class Person(models.Model):
	user=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	following=models.CharField(max_length=255)
	followed=models.CharField(max_length=255)
	directory=models.CharField(max_length=255)
