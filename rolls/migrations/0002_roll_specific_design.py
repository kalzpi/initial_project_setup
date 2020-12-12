# Generated by Django 3.0.1 on 2019-12-27 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0003_auto_20191224_1700'),
        ('rolls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roll',
            name='specific_design',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rolls', to='designs.SpecificDesign'),
        ),
    ]