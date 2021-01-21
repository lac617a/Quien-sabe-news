from django.contrib import admin
from news.models import Category,NewNews
# Register your models here.

admin.site.register(NewNews)
admin.site.register(Category)