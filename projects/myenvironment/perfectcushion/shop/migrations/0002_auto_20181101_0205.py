# Generated by Django 2.1.2 on 2018-10-31 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descripion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='descripion',
            new_name='description',
        ),
    ]
