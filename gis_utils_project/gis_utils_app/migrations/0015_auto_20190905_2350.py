# Generated by Django 2.2.4 on 2019-09-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0014_auto_20190905_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ave_age',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='service_years',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
