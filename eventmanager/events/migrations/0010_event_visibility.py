# Generated by Django 2.1.2 on 2018-12-05 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20181204_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='visibility',
            field=models.TextField(default=django.utils.timezone.now, verbose_name='visibility'),
            preserve_default=False,
        ),
    ]
