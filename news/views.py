from django.shortcuts import render,redirect,get_object_or_404
from .models import NewNews,Category,PermissionsAndPrivacy
from django.http import Http404,JsonResponse,HttpResponse
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from django.utils.http import is_safe_url
from django.conf import settings
from slugify import slugify

# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def all_recents_news_view(request,*args,**kwargs):
  return render(request,'pages/recents/all-recents.html',status=200)

def terms_and_conditions(request,*args,**kwargs):
  obj = PermissionsAndPrivacy.objects.all()
  return render(request,'pages/terms-and-conditions.html',context={'obj':obj})

def update_site_web(request,*args,**kwargs):
  pass
class PostListView(ListView):
  model = NewNews
  context_object_name = 'news_breakings'
  template_name = 'pages/home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context.update({
      'popular_hit':NewNews.objects.order_by('-hit_count_generic__hits')[:1]
    })
    return context

def get_news_category(request,*args,**kwargs):
  next_url = request.GET.get('next') or None
  item = request.GET.get('search')
  context = {}
  status = 200
  c = Category.objects.all().values('categories')
  if item != '':
    if item[::] in 'africa':
        item = 'África'
    obj = [x['categories'] for x in c if item[0].capitalize() in x['categories'][0]]
    for i in obj:
      regular_expressions = slugify(i)
      if item in regular_expressions:
        item = i
  category = Category.objects.filter(categories__iexact=item)
  if category.exists():
    first = category.first()
    context['categories'] = NewNews.objects.filter(categories_id=first.id)
  if context == {}:
    if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
      return redirect(next_url)
  return render(request,'components/form-seeker.html', context,status=status)

def search_objects(request,*args,**kwargs):
  qs = NewNews.objects.all()
  context = [x.serialize() for x in Category.objects.all()]
  data = {'response':context}
  return JsonResponse(data)