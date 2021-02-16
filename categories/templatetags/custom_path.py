from django import template
from news.models import NewNews, Category
from django.http import Http404

register = template.Library()

@register.simple_tag
def get_categories():
  qs = Category.objects.all()
  try:
    return qs
  except NewNews.DoesNotExist:
    raise Http404
