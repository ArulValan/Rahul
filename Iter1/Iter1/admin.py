from django.contrib import admin
from .models import Person

class AuthorAdmin(admin.ModelAdmin):
	admin.site.register(Person)
