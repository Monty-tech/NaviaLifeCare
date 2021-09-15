# Generated by Django 3.2.7 on 2021-09-15 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_id', models.FloatField(verbose_name='sku_id')),
                ('product_id', models.FloatField(verbose_name='product_id')),
                ('sku_name', models.CharField(max_length=200, verbose_name='sku_name')),
                ('price', models.FloatField(verbose_name='price')),
                ('manufacturer_name', models.CharField(max_length=500, verbose_name='manufacturer_name')),
                ('salt_name', models.TextField(verbose_name='salt_name')),
                ('drug_form', models.CharField(max_length=100, verbose_name='drug_form')),
                ('Pack_size', models.CharField(max_length=100, verbose_name='Pack_size')),
                ('strength', models.CharField(max_length=100, verbose_name='strength')),
                ('product_banned_flag', models.CharField(max_length=100, verbose_name='product_banned_flag')),
                ('unit', models.CharField(max_length=100, verbose_name='unit')),
                ('price_per_unit', models.FloatField(verbose_name='price_per_unit')),
            ],
        ),
    ]
