# Generated by Django 5.0.2 on 2024-04-04 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
    ]