# Generated by Django 3.2.10 on 2021-12-20 13:13

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0009_auto_20211220_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='github',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2021, 12, 20, 13, 13, 23, 142415, tzinfo=utc)),
        ),
    ]