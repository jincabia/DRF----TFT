# Generated by Django 5.0 on 2024-09-21 04:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JinsTFTAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tactician',
            name='placing',
        ),
        migrations.CreateModel(
            name='TacticianPlacements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement', models.IntegerField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JinsTFTAPI.game')),
                ('tactician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='JinsTFTAPI.tactician')),
            ],
        ),
    ]