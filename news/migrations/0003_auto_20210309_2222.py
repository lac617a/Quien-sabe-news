# Generated by Django 2.2 on 2021-03-09 22:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_motivation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newnews',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
