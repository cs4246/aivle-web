# Generated by Django 5.1.1 on 2024-09-15 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_partition_task_partition'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='gpus',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]