# Generated by Django 2.0.5 on 2018-05-19 18:38

import django.contrib.postgres.fields
from django.db import migrations, models
import jobs.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('github_profile_link', models.URLField(blank=True, verbose_name='Github Profile Link')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='Location')),
                ('job_type', models.CharField(choices=[('Full Time', 'Full-Time'), ('Part Time', 'Part-Time'), ('Contract', 'Contract')], max_length=50, verbose_name='Job Type')),
                ('apply_url', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is this job active?')),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30, verbose_name='skill'), blank=True, null=True, size=None)),
                ('expiry_date', models.DateTimeField(default=jobs.models.get_expiry_time, verbose_name='Expiry Date')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='Company')),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
                'db_table': 'job',
            },
        ),
    ]
