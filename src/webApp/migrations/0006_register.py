# Generated by Django 3.2.5 on 2021-07-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0005_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('idNumber', models.IntegerField()),
                ('PostalCode', models.IntegerField()),
                ('PostalAddress', models.IntegerField()),
                ('county', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
    ]
