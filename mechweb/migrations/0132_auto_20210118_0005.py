# Generated by Django 3.1.1 on 2021-01-17 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0131_auto_20201231_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='programspecialization',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
