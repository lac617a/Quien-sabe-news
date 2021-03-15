from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
  priority = 0.6
  
  def items(self):
    # URLs names
    return ['index','aboutus','ourstory']
  
  def location(self,item):
    return reverse(item)