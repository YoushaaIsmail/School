# Generated by Django 5.0.2 on 2024-04-04 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installment1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level1', models.FloatField()),
                ('level2', models.FloatField()),
                ('level3', models.FloatField()),
                ('level4', models.FloatField()),
                ('level5', models.FloatField()),
                ('level6', models.FloatField()),
                ('school', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='His_Installment', to='schoolapp.school')),
            ],
        ),
    ]
