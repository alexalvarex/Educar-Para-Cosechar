# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-20 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_auto_20171020_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='fin_clases',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='inicio_clases',
            field=models.DateField(blank=True, null=True),
        ),
    ]
