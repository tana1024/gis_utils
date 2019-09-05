# Generated by Django 2.2.4 on 2019-09-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gis_utils_app', '0010_client_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='ave_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='income',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='service_years',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='clientupdatestatus',
            name='status',
            field=models.CharField(choices=[('0', '未更新'), ('1', '更新開始'), ('2', '更新完了'), ('9', '異常終了')], default='0', max_length=1),
        ),
    ]
