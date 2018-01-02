# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-10 14:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0021_auto_20171108_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=70, null=True)),
                ('lugar_trabajo', models.CharField(blank=True, max_length=70, null=True)),
                ('otra_formacion', models.CharField(blank=True, max_length=70, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('formacion_academida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Formacion_Academica', to='adminapp.FormacionAcademica')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Municipio')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Sexo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Administrador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
