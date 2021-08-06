from django.db import models
from users.models import User
CHOICES = [
    ('Available', 'Available'),
    ('Out Of Stock', 'Out Of Stock'),
]
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class GroceryBag(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(upload_to = user_directory_path)
    product_price = models.CharField(max_length=20)
    product_color = models.CharField(max_length=20)
    product_category = models.ManyToManyField(Category)
    product_stock_status = models.CharField(choices=CHOICES,max_length=20)