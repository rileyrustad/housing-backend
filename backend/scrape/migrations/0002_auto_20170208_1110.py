# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craigslistposting',
            name='listed_on',
            field=models.DateField(help_text='when the craigslist listing was posted'),
        ),
    ]
