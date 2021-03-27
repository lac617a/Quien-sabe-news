from django.urls.conf import path
from rest_framework import routers
from django.urls import include
from .viewset import GenericListViews, NewsViewSet, CategoryViewSet, news_list_view,CountryViewSet

routers = routers.SimpleRouter()
routers.register('news',NewsViewSet)
routers.register('category',CategoryViewSet)
routers.register('categories',CountryViewSet)

urlpatterns = [
  path('',include((routers.urls))),
  path('generic-list/',GenericListViews.as_view()),
  path('news-list/',news_list_view),
]

# urlpatterns = routers.urls