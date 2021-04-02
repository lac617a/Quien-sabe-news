from django import template
from news.models import NewNews, Category
from datetime import datetime
from hitcount.models import HitCount

register = template.Library()

@register.simple_tag
def count_total():
  current_count = 0
  for x in HitCount.objects.all():
    current_count += x.hits
  return current_count

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
  # FORMAT
  format_date = '%d/%m/%Y %H:%M %p'
  CURR_DATATIME = datetime.now()
  CURR_TIME = CURR_DATATIME.time()
  # CURRENT DATE
  current_time = CURR_TIME.hour
  current_day = CURR_DATATIME.day
  current_month = CURR_DATATIME.month
  # TRANSFORM DATE TO STRING
  publication_date = datetime.strptime(format_string,format_date)
  get_publication_day = publication_date.date().day
  get_publication_month = publication_date.date().month
  # COMBINATION OF RETURN
  combination_date = datetime.strftime(publication_date.date(),'%d/%m/%y')
  combination_time = publication_date.time().hour
  # Manejando datos semanales
  DAY = ('Ayer','Anteayer') # hace 3/4/5/6/ y publicado hace 1 semana
  SEMANA = 7
  # print(get_publication_day)
  if current_month > get_publication_month:
    return combination_date
  elif current_day > get_publication_day:
    return combination_date
  else:
    # Aqui contamos por hora de publicacion.
    if current_time == combination_time:
      return 'publicación reciente'
    else:
      return f'publicado hace {current_time - combination_time} hora'

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
  object_filter = NewNews.objects.filter(category__iexact=u'internacional').order_by('?')[:8]
  return object_filter

#Simple llamada a la db de forma rebanada, para todas las nuevas noticias.
@register.simple_tag
def get_element_news(a,b):
  """LLamada simple al primer objecto de nuestro db"""
  object_filter = NewNews.objects.all()[a:b]
  return object_filter