# Generated by Django 3.2.8 on 2021-10-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='obj',
            field=models.FileField(blank=True, null=True, upload_to='product_obj'),
        ),
    ]
