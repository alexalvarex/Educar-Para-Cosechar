# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-19 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_grado_facilitador'),
    ]

    operations = [
        migrations.AddField(
            model_name='centro',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminapp.Municipio'),
            preserve_default=False,
        ),
    ]
