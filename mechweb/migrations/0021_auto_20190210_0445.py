# Generated by Django 2.1.5 on 2019-02-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0020_auto_20190204_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facultyhomepage',
            name='head_of_dept',
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='designation',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Assistant_Professor', 'Assistant_Professor'), ('Associate_Professor', 'Associate_Professor'), ('Visiting_Professor', 'Visiting_Professor'), ('Professor_On_lien', 'Professor_On_lien')], default='Assistant_Professor', max_length=25),
        ),
    ]
