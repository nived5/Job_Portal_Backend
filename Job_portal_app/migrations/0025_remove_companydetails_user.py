# Generated by Django 5.0.6 on 2024-08-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job_portal_app', '0024_companydetails_company_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetails',
            name='user',
        ),
    ]
