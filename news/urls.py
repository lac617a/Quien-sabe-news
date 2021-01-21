from . import views
from django.urls import path
app_name = 'News'

urlpatterns = [
  path('',views.PostListView.as_view()),
  path('<int:id_news>/<slug:slug_news>/',views.slug_view,name="slug_general"),
  path('recent-news/',views.all_recents_news_view,name="recent-news"),
]