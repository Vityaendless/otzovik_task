# Generated by Django 5.0.6 on 2024-06-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avg_grade',
            field=models.IntegerField(default=0, verbose_name='Avg grade'),
        ),
    ]