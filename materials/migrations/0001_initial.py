# Generated by Django 3.0.1 on 2019-12-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('serial_no', models.CharField(max_length=50, unique=True)),
                ('outer_dia', models.FloatField()),
                ('inner_dia', models.FloatField(blank=True, null=True)),
                ('length', models.FloatField()),
                ('drawing', models.FileField(null=True, upload_to='material/drawings/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]