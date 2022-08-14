# Generated by Django 4.0.5 on 2022-08-14 13:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0025_favourite_product_favourite_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(blank=True, default=None, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Favourite',
        ),
    ]
