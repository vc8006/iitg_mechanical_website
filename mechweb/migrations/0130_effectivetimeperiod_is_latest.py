# Generated by Django 3.1.1 on 2020-12-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0129_auto_20201231_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='effectivetimeperiod',
            name='is_latest',
            field=models.BooleanField(default=False, null=True, verbose_name='Is this latest course structure?'),
        ),
    ]
