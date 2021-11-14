# Generated by Django 3.2.8 on 2021-10-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('factoryCode', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('dimensionMin', models.IntegerField(max_length=10)),
                ('dimensionMax', models.IntegerField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('direction', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('isStandard', models.BooleanField()),
                ('group', models.IntegerField(max_length=5)),
            ],
        ),
    ]
