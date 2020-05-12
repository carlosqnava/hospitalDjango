# Generated by Django 3.0.3 on 2020-02-27 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre del estado')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre del municipio')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Estado', verbose_name='Estado')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.Estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='municipio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pacientes.Municipio', verbose_name='Municipio'),
        ),
    ]
