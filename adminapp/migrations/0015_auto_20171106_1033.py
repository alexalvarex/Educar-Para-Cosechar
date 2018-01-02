# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-06 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_remove_matricula_requisito'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('ocupacion', models.CharField(max_length=70)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('condicion', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormacionAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GradoAnterior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado_anterior', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('ocupacion', models.CharField(max_length=70)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('grupo_etnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.GrupoEtnico')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Municipio')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Sexo')),
            ],
        ),
        migrations.RemoveField(
            model_name='personas',
            name='grupo_etnico',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='tipo_persona',
        ),
        migrations.RemoveField(
            model_name='personas',
            name='trabaja',
        ),
        migrations.RenameField(
            model_name='facilitador',
            old_name='formacion_academica',
            new_name='otra_formacion',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='horario',
        ),
        migrations.AddField(
            model_name='facilitador',
            name='centro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Centro', to='adminapp.Centro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grado',
            name='horario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='matricula',
            name='requisito',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Requisito', to='adminapp.Descicion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='centro',
            name='promotor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.Promotor'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Alumno'),
        ),
        migrations.DeleteModel(
            name='Personas',
        ),
        migrations.AddField(
            model_name='alumno',
            name='grado_anterior',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GradoAnterior', to='adminapp.GradoAnterior'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='grupo_etnico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.GrupoEtnico'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Municipio'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Sexo'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='tipo_persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.TipoPersona'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='trabaja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabaja', to='adminapp.Descicion'),
        ),
        migrations.AddField(
            model_name='facilitador',
            name='formacion_academida',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='FormacionAcademica', to='adminapp.FormacionAcademica'),
            preserve_default=False,
        ),
    ]
