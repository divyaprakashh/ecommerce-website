# Generated by Django 3.2.9 on 2021-12-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productmanagement', '0007_products_category_offer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='offer_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='offer_percent',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]