# Generated by Django 5.0.6 on 2024-06-03 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, default='../static/images/tovar.png', null=True, upload_to='publications_images', verbose_name='Avatar'),
        ),
    ]
