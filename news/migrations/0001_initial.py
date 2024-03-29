# Generated by Django 2.2 on 2021-02-04 09:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Colombia', 'Colombia'), ('Internacional', 'Internacional'), ('Política', 'Política'), ('Justicia', 'Justicia'), ('Deporte', 'Deporte'), ('Tendencia', 'Tendencia'), ('Tecnología', 'Tecnología'), ('Entretenimiento', 'Entretenimiento')], default='Colombia', max_length=16, verbose_name='Categoría')),
                ('categories', models.CharField(max_length=64, unique=True, verbose_name='Nombre de la categoria')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PermissionsAndPrivacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo de privacidad')),
                ('content', models.TextField(verbose_name='contenido de privacidad')),
            ],
        ),
        migrations.CreateModel(
            name='NewNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Colombia', 'Colombia'), ('Internacional', 'Internacional'), ('Política', 'Política'), ('Justicia', 'Justicia'), ('Deporte', 'Deporte'), ('Tendencia', 'Tendencia'), ('Tecnología', 'Tecnología'), ('Entretenimiento', 'Entretenimiento')], default='Colombia', max_length=16, verbose_name='Categoría')),
                ('city', models.CharField(blank=True, help_text='Publique una cuidad si estas publicando contenido sobre una ciudad en específico.', max_length=100, null=True, unique=True, verbose_name='Ciudad del mundo')),
                ('header', models.CharField(max_length=80, verbose_name='Titulo del contenido')),
                ('sub_title', models.CharField(blank=True, help_text='Dado caso que Exista un Sub titulo', max_length=150, null=True, verbose_name='Sub titulo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news-post/%Y/%m/%d', verbose_name='Imagen del post')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido del nuevo post')),
                ('sub_content', models.TextField(blank=True, help_text='Dado caso que Exista un Sub contenido', max_length=250, null=True, verbose_name='sub contenido')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de publicación')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de edición')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('categories', models.ForeignKey(help_text='Es siempre necesario este campo', on_delete=django.db.models.deletion.CASCADE, to='news.Category')),
            ],
            options={
                'verbose_name': 'Nueva Noticia',
                'verbose_name_plural': 'Nueva Noticias',
                'ordering': ['-id'],
            },
        ),
    ]
