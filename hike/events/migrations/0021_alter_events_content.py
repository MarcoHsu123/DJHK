# Generated by Django 3.2.10 on 2022-03-22 23:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20220320_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='活动内容'),
        ),
    ]
