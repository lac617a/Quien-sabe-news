from django.urls import path
from categories.views import slug_detail_view,category_detail_view,category_list_views

urlpatterns = [
  path(route='<str:category>/<str:categories>/<slug:slug_news>/',view=slug_detail_view,name="slug-general"),
  path(route='<str:category>/<slug:categories>/', view=category_detail_view, name='all-categories'),
	path(route='<slug:category>/',view=category_list_views,name='all-category'),
]

handler404 = 'categories.views.view_404'