# Generated by Django 5.1 on 2024-08-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appinmobiliaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
                ('imagen', models.BinaryField()),
                ('precio', models.IntegerField()),
                ('tamanio', models.CharField(max_length=100)),
            ],
        ),
    ]
