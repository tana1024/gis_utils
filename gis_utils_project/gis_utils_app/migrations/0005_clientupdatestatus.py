# Generated by Django 2.2.3 on 2019-08-21 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0004_auto_20190731_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUpdateStatus',
            fields=[
                ('audit_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('status', models.CharField(default='0', max_length=1)),
                ('update_datetime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
