# Generated by Django 3.2.8 on 2021-10-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='direction',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
