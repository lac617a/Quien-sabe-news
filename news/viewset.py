from rest_framework import viewsets
from .serializer import NewsSerializer, CategorySerializer
from .models import NewNews, Category

class NewsViewSet(viewsets.ModelViewSet):
  queryset = NewNews.objects.all()
  serializer_class = NewsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer