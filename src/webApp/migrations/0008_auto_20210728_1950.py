# Generated by Django 3.2.5 on 2021-07-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_rest_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='service',
            field=models.CharField(choices=[('1', 'Individual Return'), ('2', 'Company Tax Return'), ('3', 'VAT Return Filing'), ('4', 'PAYE Return Filing')], default='Individual Return', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='dob',
            field=models.CharField(max_length=50),
        ),
    ]
