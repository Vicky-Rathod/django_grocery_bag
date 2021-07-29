from django import forms
from django.db import models
from django.db.models import fields 
from .models import GroceryBag
from parsley.decorators import parsleyfy

@parsleyfy
class GroceryBagForm(forms.ModelForm):
   class Meta:
        model= GroceryBag 
        fields = '__all__'
        exclude = ('user',)
    
        widgets = {
            'product_category': forms.Select(),
        }
        
    