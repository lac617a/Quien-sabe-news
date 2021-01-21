from django.db import models
from django.utils.timezone  import now
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=64,verbose_name='Nombre de la categoria',unique=True)
  update = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición')
  created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')

  class Meta:
    ordering = ['name']
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

  def __str__(self):
    return self.name

@python_2_unicode_compatible
class NewNews(models.Model):
  CATEGORIES = [
    ('Colombia','Colombia'),
    ('Internacional','Internacional'),
    ('Política','Política'),
    ('Justicia','Justicia'),
    ('Deporte','Deporte'),
    ('Tendencia','Tendencia'),
    ('Tecnología','Tecnología'),
    ('Entretenimiento','Entretenimiento'),
  ]
  city = models.CharField(
    max_length=100,
    help_text='Publique una cuidad si estas publicando contenido sobre una ciudad en específico.',
    verbose_name='Ciudad del mundo',
    blank=True,
    null=True,
    unique=True,
    )
  categories = models.CharField(
    max_length=16,
    choices=CATEGORIES,
    default=CATEGORIES[0][0],
    verbose_name='Categoría',
    )
  sub_categories = models.ForeignKey(to=Category,on_delete=models.CASCADE,help_text='Es siempre necesario este campo')
  title = models.CharField(max_length=80, verbose_name='Titulo del contenido')
  sub_title = models.CharField(
    max_length=150,
    null=True,
    blank=True,
    verbose_name='Sub titulo',
    help_text='Dado caso que Exista un Sub titulo'
    )
  image = models.ImageField(upload_to='news-post/%Y/%m/%d',verbose_name='Imagen del post',null=True,blank=True)
  content = RichTextField(verbose_name='Contenido del nuevo post')
  sub_content = models.TextField(
    verbose_name='sub contenido',
    null=True,
    blank=True,
    max_length=250,
    help_text='Dado caso que Exista un Sub contenido'
    )
  published = models.DateTimeField(default=now,verbose_name='Fecha de publicación')
  slug = models.SlugField(unique=True, max_length=100,blank=True)
  is_popular = models.BooleanField(verbose_name='Contenido popular',help_text='¿Seguro que el contenido es popular?',default=False)
  hit_count_generic = GenericRelation(HitCount,object_id_field='object_pk',related_query_name='hit_count_generic_releation')
  update = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición')
  created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación')

  class Meta:
    ordering = ['-id']
    verbose_name = 'Nueva Noticia'
    verbose_name_plural = 'Nueva Noticias'

  def __str__(self):
    return self.title

  @property
  def get_image_url(self):
    if self.image and hasattr(self.image,'url'):
      return self.image.url
    else:
      return '/static/img/tnews.png'

  def save(self,*args,**kwargs):
    if not self.slug:
      # Newly created object, so set slug
      self.slug = slugify(self.title)
      return super(NewNews,self).save(*args,**kwargs)

class PermissionsAndPrivacy(models.Model):
  title = models.CharField(verbose_name='Titulo de privacidad',max_length=100)
  content = models.TextField(verbose_name='contenido de privacidad')