# Generated by Django 3.0.8 on 2020-11-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
