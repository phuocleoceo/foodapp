# Generated by Django 4.0.4 on 2022-06-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]