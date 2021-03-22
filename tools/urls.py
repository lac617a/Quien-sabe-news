"""tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from news.models import NewNews
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

# add as many as sitemap you need as one key

info_dict = {'queryset':NewNews.objects.all()}

urlpatterns = [
    path('',include('news.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('Category/',include('categories.urls')),
    path('api/v0.1/',include('news.urls_router')),
    path('api/v0.1/',include('news.urls_router')),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('sitemap.xml', sitemap, {'sitemaps': {'blog':GenericSitemap(info_dict,priority=0.6,protocol='https')}},name='django.contrib.sitemaps.views.sitemap'),
    path('18-qsnoticia-forever/', admin.site.urls),
]

if settings.DEBUG: # DEV ONLY
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)