# Generated by Django 3.0.8 on 2020-11-09 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20201109_0431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clothing',
            old_name='type',
            new_name='clothing_type',
        ),
    ]
