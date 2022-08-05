# Generated by Django 4.0.5 on 2022-08-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_subscribe_alter_review_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribe',
            options={'verbose_name': 'E-mail рассылка', 'verbose_name_plural': 'E-mail рассылка'},
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
