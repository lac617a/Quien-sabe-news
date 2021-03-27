from django.contrib.contenttypes import fields
from rest_framework import serializers
from .models import NewNews, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ('id','categories')

class NewsSerializer(serializers.ModelSerializer):
  class Meta:
    model = NewNews
    fields = ('header','sub_title','image','category','categories','slug','published')