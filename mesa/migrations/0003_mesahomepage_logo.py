# Generated by Django 3.1.1 on 2020-10-31 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('mesa', '0002_auto_20201101_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesahomepage',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
