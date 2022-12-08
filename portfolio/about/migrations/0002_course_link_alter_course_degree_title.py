# Generated by Django 4.1.3 on 2022-12-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.URLField(blank=True, max_length=180),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree_title',
            field=models.CharField(max_length=150, verbose_name='Titulo obtenido'),
        ),
    ]