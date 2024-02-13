# Generated by Django 4.2.9 on 2024-01-31 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogsTypesDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('costo', models.DecimalField(decimal_places=0, default=0, max_digits=25)),
                ('dishes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.catalogstypesdishes', verbose_name='Tipo de plato')),
            ],
        ),
    ]