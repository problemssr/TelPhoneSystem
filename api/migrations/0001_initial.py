# Generated by Django 4.0.6 on 2022-08-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='phone_info',
            fields=[
                ('phone_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_name', models.TextField(verbose_name='设备类型')),
                ('phone_brand', models.CharField(max_length=64, verbose_name='设备品牌')),
                ('phone_serial_number', models.TextField(verbose_name='设备序列号')),
                ('phone_source', models.CharField(blank=True, max_length=64, null=True, verbose_name='设备来源')),
                ('phone_IMEI', models.TextField(blank=True, null=True, verbose_name='设备IMEI号')),
            ],
            options={
                'db_table': 'phone_info',
            },
        ),
    ]
