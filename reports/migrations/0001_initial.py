# Generated by Django 5.0 on 2023-12-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('result_amount', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
