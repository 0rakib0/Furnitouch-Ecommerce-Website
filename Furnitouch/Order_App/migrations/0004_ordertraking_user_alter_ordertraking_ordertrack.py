# Generated by Django 4.2.9 on 2024-03-06 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Order_App', '0003_rename_order_ordertraking_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordertraking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordertraking',
            name='OrderTrack',
            field=models.CharField(default='In Prossess', max_length=156),
        ),
    ]
