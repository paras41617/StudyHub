from django.contrib import admin
from .models import Category, Grade, Material

# Register your models here.

admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Grade)