# Generated by Django 3.2.8 on 2021-10-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dimensionMax',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='dimensionMin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.IntegerField(),
        ),
    ]
