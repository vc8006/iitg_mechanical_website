# Generated by Django 3.1.1 on 2020-12-15 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0119_auto_20201216_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectivetimeperiod',
            name='end',
            field=models.DateField(blank=True),
        ),
    ]
