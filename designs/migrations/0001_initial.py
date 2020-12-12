# Generated by Django 3.0.1 on 2019-12-19 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='PartsDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('model_name', models.CharField(max_length=200, unique=True)),
                ('part_name', models.CharField(choices=[('body', 'Body'), ('shaft', 'Shaft')], max_length=10)),
                ('outer_dia', models.FloatField()),
                ('inner_dia', models.FloatField(blank=True, null=True)),
                ('length', models.FloatField()),
                ('cutback', models.FloatField(blank=True, null=True)),
                ('drawing', models.FileField(upload_to='designs/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='designs', to='designs.Company')),
                ('main_body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs_main_body', to='designs.PartsDesign')),
                ('main_gear_shaft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs_main_gear_shaft', to='designs.PartsDesign')),
                ('main_steam_shaft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs_main_steam_shaft', to='designs.PartsDesign')),
                ('sub_body', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs_sub_body', to='designs.PartsDesign')),
                ('sub_gear_shaft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs_sub_gear_shaft', to='designs.PartsDesign')),
                ('sub_steam_shaft', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='designs_sub_steam_shaft', to='designs.PartsDesign')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]