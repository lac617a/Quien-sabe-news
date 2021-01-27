from . import views
from django.urls import path, include
app_name = 'News'

urlpatterns = [
  path('',views.PostListView.as_view()),
  path('Category/',include('news.urls_categories')),
  path('recent-news/',views.all_recents_news_view,name="recent-news"),
]