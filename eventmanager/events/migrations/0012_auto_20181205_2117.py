# Generated by Django 2.1.2 on 2018-12-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20181205_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='visibility',
            field=models.CharField(default='1', max_length=2, verbose_name='visibility'),
        ),
    ]