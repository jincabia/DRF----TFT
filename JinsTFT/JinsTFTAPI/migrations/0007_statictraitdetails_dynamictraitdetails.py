# Generated by Django 5.0 on 2024-10-06 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JinsTFTAPI', '0006_tactician_name_tactician_path_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticTraitDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait_name', models.CharField(max_length=100)),
                ('tier_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DynamicTraitDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier_current', models.IntegerField()),
                ('num_units', models.IntegerField()),
                ('style', models.IntegerField()),
                ('placement', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JinsTFTAPI.game')),
                ('static_trait_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JinsTFTAPI.statictraitdetails')),
            ],
        ),
    ]
