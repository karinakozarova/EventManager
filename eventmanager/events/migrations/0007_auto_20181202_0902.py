# Generated by Django 2.1.2 on 2018-12-02 09:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_merge_20181201_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='attendees', to=settings.AUTH_USER_MODEL, verbose_name='Attendees'),
        ),
    ]