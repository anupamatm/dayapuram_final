# Generated by Django 4.1.1 on 2022-11-10 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_addcart_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]