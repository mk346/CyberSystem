# Generated by Django 3.2.5 on 2021-07-28 14:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_apply_changedet_register_rest'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='PostalAddress',
            field=models.IntegerField(default=12000),
            preserve_default=False,
        ),
    ]