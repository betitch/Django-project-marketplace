# Generated by Django 3.2.18 on 2023-09-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20230830_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_bid',
            field=models.BooleanField(default=True, verbose_name='入札できる'),
        ),
    ]