# Generated by Django 4.2.9 on 2024-02-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_app', '0004_category_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_meterials',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.AddField(
            model_name='product',
            name='fabrics_details',
            field=models.CharField(default=1, max_length=165),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_ready_Stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='product_Colors',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='wood_details',
            field=models.CharField(default=1, max_length=165),
            preserve_default=False,
        ),
    ]