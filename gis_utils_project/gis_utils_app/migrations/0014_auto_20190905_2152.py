# Generated by Django 2.2.4 on 2019-09-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0013_auto_20190905_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ave_age',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='service_years',
            field=models.DecimalField(decimal_places=2, max_digits=2, null=True),
        ),
    ]