# Generated by Django 3.1.2 on 2021-03-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0128_mechhomepage_yt_video_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentbatch',
            options={'verbose_name': 'Student Batch', 'verbose_name_plural': 'Student Batches'},
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]