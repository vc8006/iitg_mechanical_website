# Generated by Django 2.2.1 on 2020-02-10 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0088_auto_20200209_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 9, 7, 41, 9, 224234, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='committeepage',
            name='tenure_end',
            field=models.DateField(default=datetime.datetime(2021, 2, 9, 7, 41, 9, 245687, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='leaving_year',
            field=models.DateField(default=datetime.datetime(2024, 2, 9, 7, 41, 9, 224234, tzinfo=utc)),
        ),
    ]