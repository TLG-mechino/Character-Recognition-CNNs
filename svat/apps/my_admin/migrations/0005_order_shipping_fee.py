# Generated by Django 3.2.1 on 2021-06-04 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin', '0004_auto_20210603_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_fee',
            field=models.IntegerField(default=0),
        ),
    ]
