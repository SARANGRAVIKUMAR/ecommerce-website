# Generated by Django 3.0.8 on 2020-07-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
