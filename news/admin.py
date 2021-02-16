from django.contrib import admin
from news.models import Category,NewNews,PermissionsAndPrivacy
# Register your models here.

@admin.register(NewNews)
class NewNewsAdmin(admin.ModelAdmin):
  list_display = ('header','category','categories','published')
  list_filter = ('published','city')
  date_hierarchy = 'published'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('category','categories')

@admin.register(PermissionsAndPrivacy)
class PrivacyAdmin(admin.ModelAdmin):
  pass