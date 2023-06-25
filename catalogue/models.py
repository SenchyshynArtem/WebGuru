from django.db import models
from django.urls import reverse
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="products")
    price=models.IntegerField()
    
    def get_absolute_url(self):
        return reverse('product', kwargs = {'product_pk': self.pk})
    
    
class AdditionalParameter(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    
