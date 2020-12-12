# Generated by Django 3.0.1 on 2019-12-27 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20191225_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defectreport',
            name='issued_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='inspectionreport',
            name='issued_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]