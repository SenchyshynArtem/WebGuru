from django.db import models
from catalogue.models import *

# Create your models here.
class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=32)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    additional_parameters = models.ManyToManyField(AdditionalParameter)


