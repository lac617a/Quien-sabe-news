from django import template
from django.http import Http404
from news.models import NewNews

register = template.Library()
"""
ALL CATEGORIES
"""
@register.simple_tag
def get_news_sport_news():
  """
  Un Objecto de nuestro deporte
  """
  object_filter = NewNews.objects.filter(sub_categories=5)[:1]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_main_news():
  """
  Pequena llamada a 3 objecto de las principales noticias
  """
  object_filter = NewNews.objects.all()[:3]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_the_best_news():
  """
  Cierta llamada a 9 objecto de la categoria internacional aleatoriamente
  """
  object_filter = NewNews.objects.filter(categories='Internacional').order_by('?')[:9]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_colombia_news():
  """
  Cierta llamada a un objecto de la categoria colombiano.
  """
  object_filter = NewNews.objects.filter(categories__exact=u'Colombia')[:1]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

"""
Simple llamada a la db de forma rebanada, para todas las nuevas noticias.
"""
@register.simple_tag
def get_element_news():
  """LLamada simple al primer objecto de nuestro db """
  object_filter = NewNews.objects.all()[:1]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_one_element_news():
  object_filter = NewNews.objects.all()[1:2]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_two_element_news():
  object_filter = NewNews.objects.all()[2:3]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_three_element_news():
  object_filter = NewNews.objects.all()[3:4]
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

"""
Llamadas a lo que pasa en el mundo
"""

@register.simple_tag
def get_international():
  object_filter = NewNews.objects.filter(categories__exact=u'Internacional')[:1] # get all international range 1
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_venezuela():
  object_filter = NewNews.objects.filter(sub_categories=1)[:3] # Get all Venezuela range 3
  try:
    return object_filter
  except NewNews.DoesNotExiste:
    raise Http404

@register.simple_tag
def get_united_state_news():
  object_filter = NewNews.objects.filter(sub_categories=2)[:1] # E.E.U.U
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404

@register.simple_tag
def get_entertainment_news():
  object_filter = NewNews.objects.filter(sub_categories=4)[:1] # Entred
  try:
    return object_filter
  except NewNews.DoesNotExist:
    raise Http404