from django.shortcuts import render, redirect, get_object_or_404
from news.models import NewNews, Category
# from hitcount.views import HitCountDetailView
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin
from slugify import slugify

def view_404(request,exception=None):
  return redirect('/')

# Create your views here.

def slug_detail_view(request,slug_news,*args,**kwargs):
  context = {}

  # slug_field ogic
  qs = NewNews.objects.filter(slug__iexact=slug_news)
  if qs.exists(): # Devuelve True si NewNews contiene algún resultado y False si no.
    qs = qs.first() # Devuelve el primer objeto que coincide con el conjunto de consultas.
    context['breaking_news'] = qs
    object = get_object_or_404(NewNews, pk=qs.id)
  else:
    return render(request,'pages/category.html',context=context, status=404)

  # hitcount logic
  popular_hits = context['popular_hits'] = NewNews.objects.order_by('-hit_count_generic__hits')[:3]
  hit_count = get_hitcount_model().objects.get_for_object(object)
  hits = hit_count.hits
  hitcontext = context['hitcount'] = {'pk': hit_count.pk}
  hit_count_response = HitCountMixin.hit_count(request, hit_count)
  if hit_count_response.hit_counted:
    hits = hits + 1
    hitcontext['hit_counted'] = hit_count_response.hit_counted
    hitcontext['hit_message'] = hit_count_response.hit_message
    hitcontext['total_hits'] = hits
  return render(request,'pages/category.html',context=context, status=200)

def category_list_views(request,category,*args,**kwargs):
  qs = NewNews.objects.order_by('-pk').filter(category__iexact=category)[1:]
  qs_entry_header = NewNews.objects.filter(category__iexact=category)[:1]
  return render(request,'pages/category/category_list/category_list.html',context={'category':qs,'entry_header':qs_entry_header,'title':category}, status=200)

def category_detail_view(request,categories,*args,**kwargs):
  remove_guide = categories.replace('-',' ')
  context = {'title':remove_guide}
  category = Category.objects.all()
  search_category = filter(lambda item: categories in slugify(item.categories), category)
  if search_category:
    for i in search_category:
      qs = NewNews.objects.filter(categories_id=i.id)
      context['categories'] = qs
  else:
    return render(request,'pages/category/category_details/category_details.html',context=context, status=404)
  return render(request,'pages/category/category_details/category_details.html',context=context, status=200)