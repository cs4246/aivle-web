# Generated by Django 2.2.4 on 2019-10-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='point',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
    ]
