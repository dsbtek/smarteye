# Generated by Django 2.2.15 on 2022-08-24 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20220824_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactiondata',
            name='Raw_nozzle_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]
