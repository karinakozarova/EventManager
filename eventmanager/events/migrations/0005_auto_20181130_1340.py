# Generated by Django 2.1.2 on 2018-11-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20181123_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, unique=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Title'),
        ),
    ]
