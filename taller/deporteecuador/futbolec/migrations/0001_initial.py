# Generated by Django 4.0.5 on 2022-06-14 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campeonato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campeonato', models.CharField(max_length=30)),
                ('auspiciante', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('siglas', models.CharField(max_length=3)),
                ('username', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('posicion', models.CharField(max_length=30)),
                ('dorsal', models.IntegerField()),
                ('sueldo', models.FloatField()),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elequipo', to='futbolec.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='CampeonatoEquipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.DateField()),
                ('campeonato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loscampeonatos', to='futbolec.campeonato')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='losequipos', to='futbolec.equipo')),
            ],
        ),
    ]
