from django.urls import path
from . import views
app_name = 'News'

urlpatterns = [
  path('',views.home_view),
]