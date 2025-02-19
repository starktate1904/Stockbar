# Generated by Django 5.0.7 on 2024-11-03 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_description_product_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='make',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('LOTIONS', 'Lotions'), ('CREAMS', 'Creams'), ('CLOTHING', 'Clothing'), ('SHOES', 'Shoes'), ('COSMETICS', 'Cosmetics'), ('HAIR', 'Hair'), ('OTHER', 'Other')], max_length=50),
        ),
    ]
