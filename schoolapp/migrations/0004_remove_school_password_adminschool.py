# Generated by Django 5.0.2 on 2024-04-11 17:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_school_password_alter_school_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='password',
        ),
        migrations.CreateModel(
            name='adminSchool',
            fields=[
                ('schoolawaremodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schoolapp.schoolawaremodel')),
                ('Competence', models.CharField(max_length=50)),
                ('account', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('schoolapp.schoolawaremodel',),
        ),
    ]