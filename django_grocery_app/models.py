from django.db import models

CHOICES = [
    ('Bought', 'BOUGHT'),
    ('Pending', 'PENDING'),
    ('Not Available', 'NOT AVAILABLE'),
]

# Create your models here.
class GroceryBag(models.Model):
    product_name = models.CharField(max_length=20)
    product_quantity = models.CharField(max_length=20)
    product_flag = models.CharField(choices=CHOICES,max_length=20)
    product_date = models.DateField()