# Generated by Django 4.0.6 on 2022-08-23 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_borrow_history_borrow_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone_info',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.borrow_info', to_field='phone', verbose_name='用户表'),
        ),
        migrations.AlterField(
            model_name='borrow_info',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='设备id'),
        ),
    ]
