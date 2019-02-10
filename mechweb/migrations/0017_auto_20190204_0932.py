# Generated by Django 2.1.5 on 2019-02-04 09:32

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0016_facultyhomepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultypublicationdocument',
            name='abstract',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='facultypublicationdocument',
            name='link',
            field=models.URLField(blank=True, max_length=250),
        ),
    ]
