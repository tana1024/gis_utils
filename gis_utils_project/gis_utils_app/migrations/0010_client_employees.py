# Generated by Django 2.2.4 on 2019-09-01 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0009_clientupdatestatus_update_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='employees',
            field=models.IntegerField(null=True),
        ),
    ]
