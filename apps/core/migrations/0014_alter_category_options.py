# Generated by Django 4.0.5 on 2022-08-02 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_message_alter_productimage_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-updated', '-created'), 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
