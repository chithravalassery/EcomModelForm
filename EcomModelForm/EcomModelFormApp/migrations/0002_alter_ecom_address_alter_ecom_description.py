# Generated by Django 5.1 on 2024-10-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomModelFormApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecom',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ecom',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
