# Generated by Django 4.0.5 on 2022-07-02 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_cart_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
