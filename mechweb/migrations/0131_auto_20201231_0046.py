# Generated by Django 3.1.1 on 2020-12-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0130_effectivetimeperiod_is_latest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effectivetimeperiod',
            name='is_latest',
            field=models.BooleanField(default=False, verbose_name='Is this latest course structure?'),
        ),
    ]