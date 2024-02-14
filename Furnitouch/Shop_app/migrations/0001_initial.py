# Generated by Django 4.2.9 on 2024-02-14 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category_name', models.CharField(max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=260)),
                ('product_code', models.CharField(max_length=20)),
                ('product_quintity', models.IntegerField(default=0)),
                ('roduct_title', models.CharField(max_length=260)),
                ('product_meterials', models.TextField()),
                ('product_keyword', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='products')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('details', models.TextField()),
                ('lenth', models.CharField(max_length=30)),
                ('Width', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=30)),
                ('main_price', models.IntegerField()),
                ('is_newarival', models.BooleanField(default=False)),
                ('is_discount', models.BooleanField(default=False)),
                ('dic_price', models.IntegerField(blank=True, default=0, null=True)),
                ('cerated_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Shop_app.category')),
                ('product_main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop_app.main_category')),
            ],
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='Shop_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductMoreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='products')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pro_mul_ing', to='Shop_app.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Shop_app.subcategory'),
        ),
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_cat', to='Shop_app.main_category'),
        ),
    ]
