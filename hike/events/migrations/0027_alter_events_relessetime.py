# Generated by Django 3.2.10 on 2022-03-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0026_auto_20220327_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='relesseTime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='发布时间'),
        ),
    ]
