# Generated by Django 5.0 on 2023-12-18 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='result_amount',
            new_name='report_amount',
        ),
    ]