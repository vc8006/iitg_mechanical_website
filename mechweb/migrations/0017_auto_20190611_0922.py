# Generated by Django 2.2.1 on 2019-06-11 09:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('mechweb', '0016_auto_20190611_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchLabHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'Lab Home',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='pages',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='pub_journal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='pub_year',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='vol_issue',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='PublicationPageOtherAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=100)),
                ('organization', models.CharField(blank=True, max_length=100)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_authors', to='mechweb.PublicationPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
