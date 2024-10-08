# Generated by Django 5.0.6 on 2024-07-03 05:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_portal_app', '0011_add_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save_jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_jobs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job_portal_app.add_job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
