# Generated by Django 5.0.3 on 2024-03-29 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='movie',
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movie.video'),
        ),
    ]
