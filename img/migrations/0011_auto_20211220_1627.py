# Generated by Django 3.2.10 on 2021-12-20 13:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0010_alter_github_added_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='github',
            name='repo_count',
        ),
        migrations.AlterField(
            model_name='github',
            name='added_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=datetime.datetime(2021, 12, 20, 13, 27, 2, 2060, tzinfo=utc)),
        ),
    ]