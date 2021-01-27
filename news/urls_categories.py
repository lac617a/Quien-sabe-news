from django.urls import path
from . import views

urlpatterns = [
  path(route='<categories>/<slug:slug_news>/',view=views.slug_view_detail,name="slug_general"),
]