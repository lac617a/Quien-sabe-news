from django.contrib.contenttypes import fields
from rest_framework import serializers
from .models import NewNews, Category

class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = NewNews
    fields = '__all__'
    ordering = ["-id"]

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'