# Generated by Django 4.2.9 on 2024-03-01 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order_App', '0002_ordertraking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordertraking',
            old_name='order',
            new_name='orderId',
        ),
    ]
