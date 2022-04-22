# Generated by Django 4.0.4 on 2022-04-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
        ),
    ]
