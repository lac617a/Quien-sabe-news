from .views import (PostListView,all_recents_news_view,search_objects,get_news_category,terms_and_conditions,update_site_web)
from django.urls import path, include

app_name = 'News'

""" TODO 
Aqui conformaremos solo la mas necesario para listado de vista simple con su respectiva clase.
Tenemos los siquiente:

* PostListView:
  * Vista lista con ListView(page main)

"""
urlpatterns = [
  path('',PostListView.as_view()),
  path('recent-news/',all_recents_news_view,name="recent-news"),
  path('deatils/',search_objects),
  path('seeker/',search_objects),
  path('get-news-category/',get_news_category),
  path('terminos-y-condiciones/',terms_and_conditions),
  path('estamos-trabajando-para-darte-la-mejor-experiencia/',update_site_web),
]