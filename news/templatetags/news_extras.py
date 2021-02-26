from django import template
from django.http import Http404
from news.models import NewNews, Category
import pyshorteners

from datetime import datetime,date,time

import six
from django_bitly.models import Bittle
from django_bitly.exceptions import BittleException

register = template.Library()

@register.filter
def bitlify(value):
    """
    Gets or create a Bittle object for the passed object. If unable to get
    Bittle and/or create bit.ly, will just return the get_absolute_url value.
    """

    try:
        bittle = Bittle.objects.bitlify(value)
        if bittle:
            url = bittle.shortUrl
        else:
            url = value.get_absolute_url
        return url
    except (BittleException, Bittle.DoesNotExist):
        if isinstance(value, six.string_types):
            return value
        else:
            return value.get_absolute_url()

@register.simple_tag
def decode_url(url):
  shortener = pyshorteners.Shortener()
  short_url = shortener.dagd.short('https://qsn.herokuapp.com'+url)
  print(short_url)
  return short_url

@register.simple_tag
def check_date_time(format_string):
  """
  Calculando la fecha y hora entrante dado caso que la hora ya haya pasado tendria que sumarle mas uno a cada hora
  hasta cumplir las 24 hora, pasara hacer fecha del ayer asi como 15/02/2021 dado caso que hoy es 16/02/2021.

  Formato para todo sobre fecha:

  milisengudo = 60000 MS
  minuto = 60 S
  hora = 60 M o 3600 S
  dia = 24 H
  """
  # H:m A HTML > %H:%M %p python
  format_date = '%d/%m/%Y %H:%M %p'
  curr_datetime = datetime.now()
  curr_time = curr_datetime.time()
  now_time = curr_time.hour
  now_date = curr_datetime.day
  present = datetime.strptime(format_string,format_date)
  last_date = present.date().day
  combination_date = datetime.strftime(present.date(),'%d/%m/%Y')
  combination_time = present.time().hour

  if now_date > last_date:
    return combination_date
  elif now_date == 1 and last_date in [28,30,31]:
    return combination_date
  else:
    if now_time == combination_time:
      return 'publicación reciente'
    else:
      return f'publicado hace {curr_time.hour - combination_time} hora'

#!hits_count_context_all
@register.simple_tag
def populares_hit(value):
  popular_hit = NewNews.objects.order_by('-hit_count_generic__hits')[:value]
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