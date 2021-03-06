# Generated by Django 2.0.4 on 2018-05-07 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0067_profile_hide_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='hide_profile',
            field=models.BooleanField(default=True, help_text='If this option is chosen, we will remove your profile information all_together'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
