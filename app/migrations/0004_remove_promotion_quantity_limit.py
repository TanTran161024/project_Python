# Generated by Django 5.1.3 on 2024-12-24 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_promotion_options_promotion_quantity_limit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='quantity_limit',
        ),
    ]
