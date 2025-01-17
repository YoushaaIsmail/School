# Generated by Django 5.0.2 on 2024-04-13 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0007_ads_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='Location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='His_location', to='schoolapp.location'),
        ),
    ]
