# Generated by Django 4.1.7 on 2023-05-24 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_app', '0005_main_category_alter_subcategory_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Shop_app.main_category'),
            preserve_default=False,
        ),
    ]
