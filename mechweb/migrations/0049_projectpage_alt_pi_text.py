# Generated by Django 2.2.1 on 2019-07-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0048_auto_20190718_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='alt_PI_text',
            field=models.CharField(blank=True, help_text="Use this only if you can't add faculty and other authors above", max_length=1000),
        ),
    ]
