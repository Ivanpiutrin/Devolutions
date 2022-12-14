# Generated by Django 4.1 on 2022-12-02 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DevolucionCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('celular', models.PositiveIntegerField()),
                ('cantidad', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('NombreVendedor', models.CharField(max_length=100)),
                ('distribuidor', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
    ]
