# Generated by Django 4.0.2 on 2022-03-07 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_employee_daily_salary_employee_hourly_wage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='daily_salary',
            new_name='time_work',
        ),
    ]
