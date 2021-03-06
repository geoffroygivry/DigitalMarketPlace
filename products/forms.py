from django import forms
from .models import Product

from django.utils.text import slugify

##################################################################################
## class ModelForm
##################################################################################


class ProductModelForm(forms.ModelForm):
  # Adding custom attributes on top of the class Meta, is overriding them (the widgets variable in class Meta is not anymore in use.)
  title = forms.CharField(label="", widget=forms.TextInput(
      attrs={
        "class" : "title-class",
        "placeholder": "Title"
      }
    ))
  description = forms.CharField(label="", widget=forms.Textarea(
        attrs={
          "class": "my-custom-class",
          "placeholder": "Description",
          "myAttr": "Geoff"
      }
    ))
  
  class Meta:
    model = Product
    fields = ['title', 'description', 'price']
    widgets = {
      "description": forms.Textarea(attrs={
          'placeholder' : 'new description',
          'class' : 'this-is-my-class'
        }
      ),
      "title" : forms.TextInput(attrs={
          "placeholder" : "Title Here"
        }
     ),
    }
    
    
  def clean(self, *args, **kwargs):
    cleaned_data = super(ProductModelForm, self).clean(*args, **kwargs)
#     title = cleaned_data.get("title")
#     slug = slugify(title)
#     qs = Product.objects.filter(slug=slug).exists()
#     if qs:
#       raise forms.ValidationError("This title is taken, please be creative and create a new one!")
    return cleaned_data
  
  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price <= 1.00 :
      raise forms.ValidationError('Price must be greater than $1.00')
    elif price >= 99.99 : 
      raise forms.ValidationError('Price must be less than $100.00')
    else:
     return price
  
  def clean_title(self):
    title = self.cleaned_data.get('title')
    if len(title) > 3 :
      return title
    else:
      raise forms.ValidationError('Title must be longer than 3 characters!')