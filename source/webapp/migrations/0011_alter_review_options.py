# Generated by Django 5.0.6 on 2024-06-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_product_avg_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': [('see_no_moderate_reviews', 'Can see no moderates reviews'), ('accept_review', 'Can accept review'), ('decline_review', 'Can decline review')]},
        ),
    ]
