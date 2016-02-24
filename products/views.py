from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Product
from .forms import ProductModelForm

from digitalmarket.mixins import MultiSlugMixin, SubmitButtonMixin
# Create your views here.


########################################################################################################  
## class Based views
########################################################################################################  

class ProductCreateView(SubmitButtonMixin, CreateView):
  model = Product
  template_name = "form.html"
  form_class = ProductModelForm
  success_url = '/products/'
  submit_button = 'Add Product'
    
##################################################################

class ProductUpdateView(SubmitButtonMixin, MultiSlugMixin, UpdateView):
  model = Product
  template_name = "form.html"
  form_class = ProductModelForm
  success_url = '/products/'
  submit_button = 'Update Product'

  
##################################################################

class ProductDetailView(MultiSlugMixin, DetailView):
  model = Product
  
##################################################################
  
class ProductListView(ListView):
  model = Product
  
  def get_queryset(self, *args, **kwargs):
      qs = super(ProductListView, self).get_queryset(**kwargs)
      return qs
  

########################################################################################################  
## Function base views  
########################################################################################################  


def create_view(request):
  # view of 1 item
  if request.user.is_authenticated():
      form = ProductModelForm(request.POST or None)
      if form.is_valid():
        instance = form.save(commit=False)
        instance.sale_price = instance.price
        instance.save()
      template = 'form.html'
      context = {
        "form" : form,
        "submit_button" : "Create Product",
      }
  else:
    template = 'not_found.html'
    context = {}
  return render(request, template, context)

##################################################################

def update_view(request, object_id=None):
  # view of 1 item
  if object_id is not None:
    if request.user.is_authenticated():
        product = get_object_or_404(Product, id=object_id)
        form = ProductModelForm(request.POST or None, instance=product)
        if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
        template = 'form.html'
        context = {
          "product" : product, 
          "form" : form,
          "submit_button" : "Update Product",
        }
    else:
      template = 'not_found.html'
      context = {}
    return render(request, template, context)
  else:
    raise Http404

##################################################################

def detail_slug_view(request, slug=None):
  # view of 1 item
  if request.user.is_authenticated():
      product = get_object_or_404(Product, slug=slug)
      template = 'detail_view.html'
      context = {
        "product" : product
      }
  else:
    template = 'not_found.html'
    context = {}
  return render(request, template, context)

##################################################################

def detail_view(request, object_id=None):
  # view of 1 item
  if object_id is not None:
    if request.user.is_authenticated():
        product = get_object_or_404(Product, id=object_id)
        template = 'detail_view.html'
        context = {
          "product" : product
        }
    else:
      template = 'not_found.html'
      context = {}
    return render(request, template, context)
  else:
    raise Http404
  
##################################################################

def list_view(request):
  # view of multiple items
  queryset = Product.objects.all()
  print request
  template = 'list_view.html'
  context = {
    'queryset': queryset
  }
  return render(request, template, context)

