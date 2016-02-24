from django.shortcuts import get_object_or_404

class MultiSlugMixin(object):
  model = None
  
  def get_object(self, *args, **kwargs):
    slug = self.kwargs.get("slug")
    ModelClass = self.model
    if slug is not None:
      try:
        obj = get_object_or_404(ModelClass, slug=slug)
      except ModelClass.MultipleObjectsReturned:
        obj = ModelClass.objects.filter(slug=slug).order_by('-title').first()
    else:
      obj = super(MultiSlugMixin, self).get_object(*args, **kwargs)
    return obj
  
  
  
class SubmitButtonMixin(object):
  submit_button = None
  def get_context_data(self, *args, **kwargs):
    context = super(SubmitButtonMixin, self).get_context_data(*args, **kwargs)
    context['submit_button'] = self.submit_button
    return context