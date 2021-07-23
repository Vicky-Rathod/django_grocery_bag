from django import forms
from django.db import models
from django.db.models import fields 
from .models import GroceryBag

class GroceryBagForm(forms.ModelForm):
   class Meta:
        model= GroceryBag 
        fields = '__all__'
    
    