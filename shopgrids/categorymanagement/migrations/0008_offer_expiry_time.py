# Generated by Django 3.2.9 on 2021-12-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanagement', '0007_auto_20211202_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='expiry_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]