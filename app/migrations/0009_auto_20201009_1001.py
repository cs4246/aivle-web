# Generated by Django 2.2.4 on 2020-10-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200823_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
