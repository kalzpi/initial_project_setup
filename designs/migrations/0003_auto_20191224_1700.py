# Generated by Django 3.0.1 on 2019-12-24 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_initiator'),
        ('designs', '0002_auto_20191223_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partsdesign',
            old_name='part_name',
            new_name='part_type',
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='partsdesign',
            name='drawing',
            field=models.FileField(upload_to='designs/partial/'),
        ),
        migrations.CreateModel(
            name='SpecificDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('drawing', models.FileField(upload_to='designs/specific/')),
                ('lot_no', models.CharField(max_length=50, unique=True)),
                ('finish_od', models.FloatField(blank=True, null=True)),
                ('od_tolerance', models.FloatField(blank=True, null=True)),
                ('number_of_teeth', models.FloatField(blank=True, null=True)),
                ('flute_type', models.CharField(blank=True, max_length=10, null=True)),
                ('flute_height', models.FloatField(blank=True, null=True)),
                ('flute_height_tolerance', models.FloatField(blank=True, null=True)),
                ('pitch', models.FloatField(blank=True, null=True)),
                ('radius_1', models.FloatField(blank=True, null=True)),
                ('radius_1_tolerance', models.FloatField(blank=True, null=True)),
                ('radius_2', models.FloatField(blank=True, null=True)),
                ('radius_2_tolerance', models.FloatField(blank=True, null=True)),
                ('take_up_ratio', models.FloatField(blank=True, null=True)),
                ('crown', models.FloatField(blank=True, null=True)),
                ('crown_tolerance', models.FloatField(blank=True, null=True)),
                ('base_design', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='SpecificDesign', to='designs.Design')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='designs', to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]