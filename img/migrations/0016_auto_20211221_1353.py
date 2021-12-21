# Generated by Django 3.2.10 on 2021-12-21 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0015_auto_20211221_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='github',
            name='repo_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='github',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2021, 12, 21, 10, 53, 3, 47975, tzinfo=utc)),
        ),
    ]
