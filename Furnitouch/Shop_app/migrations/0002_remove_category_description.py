# Generated by Django 3.2.19 on 2023-06-18 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]