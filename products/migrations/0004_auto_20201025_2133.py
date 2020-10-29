# Generated by Django 3.1.1 on 2020-10-25 18:03

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201024_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.FileField(null=True, upload_to=products.models.media_upload_path),
        ),
    ]
