# Generated by Django 4.2.9 on 2024-02-14 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_app', '0003_remove_product_product_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=1, upload_to='category_Pic'),
            preserve_default=False,
        ),
    ]