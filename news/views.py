from django.views import generic
from hitcount.views import HitCountDetailView
from django.shortcuts import render
from django.http import Http404
from .models import NewNews

# Create your views here.

def get_id_db(id):
  get_id = NewNews.objects.get(pk=id)
  try:
    return get_id
  except NewNews.DoesNotExist:
    raise Http404

# def post_list_view(request):
#   news_category = NewNews.objects.filter(categories=3)[:2]
#   news_united_state = NewNews.objects.filter(categories=4)[:1]
#   context = {"news_category":news_category,"news_united_state":news_united_state}
#   return render(request,'pages/home.html',context=context)

class PostListView(generic.ListView):
  model = NewNews
  context_object_name = 'news_sport'
  template_name = 'pages/home.html'

  def get_queryset(self,*args,**kwargs):
    qs = super(PostListView,self).get_queryset(*args,**kwargs)
    qs = qs.filter(sub_categories=5)[:1]
    return qs

def slug_view(request,slug_news,id_news,*args,**kwargs):
  breaking_news = get_id_db(id=id_news)
  return render(request,'pages/breaking-news/breaking-news.html',context={'breaking_news':breaking_news}, status=200)

def all_recents_news_view(request,*args,**kwargs):
  return render(request,'pages/recents/all-recents.html',status=200)

# class PostCountHitDetailView(post_list_view, HitCountDetailView):
#     """
#     Generic hitcount class based view that will also perform the hitcount logic.
#     """
#     count_hit = True