# Generated by Django 2.2.15 on 2022-08-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20220825_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartSolarData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac_address', models.CharField(blank=True, max_length=250, null=True, unique=True)),
                ('log_time', models.DateTimeField()),
                ('battery_voltage', models.CharField(blank=True, max_length=250, null=True)),
                ('solar_voltage', models.CharField(blank=True, max_length=250, null=True)),
                ('grid_voltage', models.CharField(blank=True, max_length=250, null=True)),
                ('output', models.CharField(blank=True, max_length=250, null=True)),
                ('previous_day_solar_unit', models.CharField(blank=True, max_length=250, null=True)),
                ('solar_status', models.CharField(blank=True, max_length=250, null=True)),
                ('today_total_solar', models.CharField(blank=True, max_length=250, null=True)),
                ('today_solar_consume_for_charging', models.CharField(blank=True, max_length=250, null=True)),
                ('solar_current', models.CharField(blank=True, max_length=250, null=True)),
                ('grid_state', models.CharField(blank=True, max_length=250, null=True)),
                ('today_solar_consume_for_load', models.CharField(blank=True, max_length=250, null=True)),
                ('total_charging_current', models.CharField(blank=True, max_length=250, null=True)),
                ('today_battery_consume_for_load', models.CharField(blank=True, max_length=250, null=True)),
                ('discharging_current', models.CharField(blank=True, max_length=250, null=True)),
                ('today_grid_consume_for_charging', models.CharField(blank=True, max_length=250, null=True)),
                ('today_load_on_grid', models.CharField(blank=True, max_length=250, null=True)),
                ('instantaneous_solar_power', models.CharField(blank=True, max_length=250, null=True)),
                ('load_on', models.CharField(blank=True, max_length=250, null=True)),
                ('output_voltage', models.CharField(blank=True, max_length=250, null=True)),
                ('output_current', models.CharField(blank=True, max_length=250, null=True)),
                ('output_power', models.CharField(blank=True, max_length=250, null=True)),
                ('output_energy', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
