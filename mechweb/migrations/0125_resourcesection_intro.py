# Generated by Django 3.1.2 on 2021-03-03 14:33

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0124_remove_resource_faculty_incharge'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcesection',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]