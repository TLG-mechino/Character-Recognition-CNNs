# Generated by Django 3.2.1 on 2021-06-30 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_admin', '0017_auto_20210625_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
