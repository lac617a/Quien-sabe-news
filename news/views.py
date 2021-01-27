from django.views import generic
from hitcount.views import HitCountDetailView
from django.shortcuts import render
from django.http import Http404, HttpResponse
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
  context_object_name = 'news_breakings'
  template_name = 'pages/home.html'

  def get_queryset(self,*args,**kwargs):
    qs = super(PostListView,self).get_queryset(*args,**kwargs)
    qs = qs.all()[:3]
    return qs

# class Slug_view_detail(generic.DetailView):
#   """Detail News."""
#   template_name = 'pages/breaking-news/breaking-news.html'
#   model = NewNews
#   context_object_name = 'breaking_news'
#   slug_field = 'slug'
#   slug_url_kwarg = 'slug_news'

def slug_view_detail(request,slug_news,*args,**kwargs):
  qs = NewNews.objects.filter(slug__iexact=slug_news)
  context = {}
  if qs.exists(): # Devuelve True si NewNews contiene algún resultado y False si no.
    qs = qs.first() # Devuelve el primer objeto que coincide con el conjunto de consultas.
  else:
    return render(request,'pages/breaking-news/breaking-news.html',context=context, status=404)
  context['breaking_news'] = qs
  return render(request,'pages/breaking-news/breaking-news.html',context=context, status=200)

def all_recents_news_view(request,*args,**kwargs):
  return render(request,'pages/recents/all-recents.html',status=200)

# class PostCountHitDetailView(post_list_view, HitCountDetailView):
#     """
#     Generic hitcount class based view that will also perform the hitcount logic.
#     """
#     count_hit = True