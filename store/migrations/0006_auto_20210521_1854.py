# Generated by Django 3.2.3 on 2021-05-21 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]