# Generated by Django 4.1.2 on 2022-10-28 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_addcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]