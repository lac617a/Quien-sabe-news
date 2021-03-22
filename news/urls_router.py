from rest_framework import routers
from .viewset import NewsViewSet, CategoryViewSet

routers = routers.SimpleRouter()
routers.register('news',NewsViewSet)
routers.register('category',CategoryViewSet)

urlpatterns = routers.urls