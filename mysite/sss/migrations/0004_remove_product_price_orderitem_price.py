# Generated by Django 4.1.7 on 2024-04-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0003_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]