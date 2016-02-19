from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
  title = models.CharField(max_length=30) # title string creation
  description = models.TextField()
  price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True, blank=True)
  sale_price = models.DecimalField(max_digits=100, decimal_places=2, default= 6.99, null=True, blank=True)
  
  def __str__(self):
    return self.title # returns the title name of the product when you print the object