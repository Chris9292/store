# Generated by Django 3.2.8 on 2021-10-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20211030_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dimensionMax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimensionMin',
            field=models.IntegerField(null=True),
        ),
    ]
