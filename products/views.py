from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductAddForm
# Create your views here.


def create_view(request):
  # view of 1 item
  if request.user.is_authenticated():
      form = ProductAddForm(request.POST or None)
      if form.is_valid():
        data = form.cleaned_data
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')
        new_product = Product.objects.create(title=title, description=description, price=price)
      template = 'create_view.html'
      context = {
        "form" : form
      }
  else:
    template = 'not_found.html'
    context = {}
  return render(request, template, context)


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

def list_view(request):
  # view of multiple items
  queryset = Product.objects.all()
  print request
  template = 'list_view.html'
  context = {
    'queryset': queryset
  }
  return render(request, template, context)

