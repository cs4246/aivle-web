# Generated by Django 2.2.4 on 2019-11-10 04:05

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_similarity'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='template',
            field=models.FileField(blank=True, null=True, upload_to=app.models.task_path),
        ),
        migrations.AddField(
            model_name='task',
            name='template_file',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
