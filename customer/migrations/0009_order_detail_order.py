# Generated by Django 4.1.2 on 2022-12-30 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_rename_price_order_amount_remove_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='customer.order'),
        ),
    ]
