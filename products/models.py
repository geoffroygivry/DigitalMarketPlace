from __future__ import unicode_literals
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.db import models

# Create your models here.

class Product(models.Model):
  title = models.CharField(max_length=30) # title string creation
  slug = models.SlugField(blank=True)
  description = models.TextField()
  price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99, null=True, blank=True)
  sale_price = models.DecimalField(max_digits=100, decimal_places=2, default= 6.99, null=True, blank=True)
  
  def __str__(self):
    return self.title # returns the title name of the product when you print the object
  
def product_pre_save_receiver(sender, instance, *args, **kwargs):
  if not instance.slug:
    instance.slug = slugify(instance.title)
    
    
pre_save.connect(product_pre_save_receiver, sender=Product)