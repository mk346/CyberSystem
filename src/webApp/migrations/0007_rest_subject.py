# Generated by Django 3.2.5 on 2021-07-28 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0006_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='rest',
            name='subject',
            field=models.CharField(default='Booking', max_length=500),
            preserve_default=False,
        ),
    ]
