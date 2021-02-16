from django import template
from django.http import Http404
from news.models import NewNews, Category

from datetime import datetime,date

register = template.Library()

@register.simple_tag
def check_date_time(format_string):
  now_date = datetime.now().day
  print(format_string)

#!hits_count_context_all
@register.simple_tag
def popular_hit():
  popular_hit = NewNews.objects.order_by('-hit_count_generic__hits')[:1]
  return popular_hit

#!ALL CATEGORIES
@register.simple_tag
def get_category_all(category):
  object_filter = NewNews.objects.filter(category__iexact=category)[:1] # get all international range 1
  return object_filter
@register.simple_tag
def get_categories(category):
  """Obtenemos las categorias y sus items. para el navbar"""
  qs = Category.objects.filter(category__iexact=category)
  return qs
@register.simple_tag
def get_categories_by_id(categories_id,value):
  object_filter = NewNews.objects.filter(categories_id=categories_id)[:value] # get_categories_by_id range 3
  return object_filter

@register.simple_tag
def get_main_news():
  """Pequena llamada a 3 objecto de las principales noticias ASIDE SLUG"""
  object_filter = NewNews.objects.all()[:3]
  return object_filter

@register.simple_tag
def get_the_best_news():
  """Cierta llamada a 9 objecto de la categoria internacional aleatoriamente"""
  object_filter = NewNews.objects.filter(category__iexact=u'internacional').order_by('?')[:9]
  return object_filter

#Simple llamada a la db de forma rebanada, para todas las nuevas noticias.
@register.simple_tag
def get_element_news(a,b):
  """LLamada simple al primer objecto de nuestro db"""
  object_filter = NewNews.objects.all()[a:b]
  return object_filter