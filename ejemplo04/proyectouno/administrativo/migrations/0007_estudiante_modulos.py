# Generated by Django 3.2.4 on 2021-06-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0006_auto_20210611_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='modulos',
            field=models.ManyToManyField(through='administrativo.Matricula', to='administrativo.Modulo'),
        ),
    ]
