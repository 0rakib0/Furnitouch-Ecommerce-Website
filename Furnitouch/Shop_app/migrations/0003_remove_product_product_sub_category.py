# Generated by Django 4.2.9 on 2024-02-14 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_app', '0002_product_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_sub_category',
        ),
    ]