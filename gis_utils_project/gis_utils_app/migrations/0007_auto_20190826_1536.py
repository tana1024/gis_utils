# Generated by Django 2.2.3 on 2019-08-26 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0006_auto_20190826_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=7, default='', max_digits=10),
        ),
        migrations.AlterField(
            model_name='client',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=7, default='', max_digits=10),
        ),
    ]