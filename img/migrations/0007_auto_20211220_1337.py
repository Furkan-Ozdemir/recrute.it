# Generated by Django 3.2.10 on 2021-12-20 10:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0006_alter_github_added_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='github',
            name='alt',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='github',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2021, 12, 20, 10, 37, 8, 354560, tzinfo=utc)),
        ),
    ]