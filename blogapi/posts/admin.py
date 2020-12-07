from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
	pass