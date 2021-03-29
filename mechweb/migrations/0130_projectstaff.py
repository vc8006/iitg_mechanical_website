# Generated by Django 3.1.2 on 2021-03-29 11:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mechweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('mechweb', '0129_auto_20210325_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStaff',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('full_name', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('joining_year', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1994), mechweb.models.max_value_current_year])),
                ('project_title', models.TextField(blank=True, null=True)),
                ('associate_faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='associate_faculty', to='mechweb.facultypage')),
            ],
            options={
                'verbose_name': 'Project Staff',
                'verbose_name_plural': 'Project Staff',
            },
            bases=('wagtailcore.page',),
        ),
    ]
