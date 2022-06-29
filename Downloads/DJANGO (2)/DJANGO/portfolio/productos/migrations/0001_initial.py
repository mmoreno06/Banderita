# Generated by Django 4.0.5 on 2022-06-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('disponible', models.BooleanField()),
                ('fechaIncorporacion', models.DateField()),
                ('correoProveedor', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=30)),
                ('suscrito', models.BooleanField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
    ]