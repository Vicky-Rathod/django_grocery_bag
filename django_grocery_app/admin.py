from django.contrib import admin
from .models import Category, GroceryBag
# Register your models here.
admin.site.register(GroceryBag)
admin.site.register(Category)