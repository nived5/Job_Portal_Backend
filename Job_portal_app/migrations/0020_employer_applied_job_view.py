# Generated by Django 5.0.6 on 2024-08-07 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_portal_app', '0019_add_qualification_delete_employer_applied_job_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='employer_applied_job_view',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job_portal_app.job_application2')),
            ],
        ),
    ]
