# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-20 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_matricula_requisito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_periodo', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='primer_periodo',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='segundo_periodo',
        ),
        migrations.AddField(
            model_name='matricula',
            name='num_periodo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Num_Periodo', to='adminapp.Periodo'),
            preserve_default=False,
        ),
    ]
