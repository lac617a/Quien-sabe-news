from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from .serializer import NewsSerializer, CategorySerializer
from .models import NewNews, Category
from rest_framework.renderers import JSONRenderer
    
class CountryViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = NewNews.objects.all()
  serializer_class = NewsSerializer
  model = NewNews

class NewsViewSet(viewsets.ModelViewSet):
  queryset = NewNews.objects.all()
  serializer_class = NewsSerializer

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def news_list_view(request):
  # qs = NewNews.objects.all()
  serializer = NewsSerializer()
  data = serializer.data
  print(data)
  return Response(data)

class GenericListViews(ListAPIView):
  queryset = NewNews.objects.all()
  serializer_class = NewsSerializer
  renderer_classes = [JSONRenderer]

class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer