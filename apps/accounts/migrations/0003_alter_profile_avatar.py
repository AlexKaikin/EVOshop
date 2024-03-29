# Generated by Django 4.0.5 on 2022-07-19 17:03

import apps.accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to=apps.accounts.models.get_avatar_file_path, verbose_name='Ваше фото'),
        ),
    ]
