# Generated by Django 5.1.1 on 2024-09-23 05:36

import app.models.group
import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models
from app.models import Group as AppGroup


def create_default_group_if_not_exist(apps, schema_editor):
    Group = apps.get_model("app", "Group")
    if not Group.objects.filter(name=AppGroup.DEFAULT).exists():
        Group.objects.create(name=AppGroup.DEFAULT)


def add_default_group_to_invitation(apps, schema_editor):
    Group = apps.get_model("app", "Group")
    Invitation = apps.get_model("app", "Invitation")
    Invitation.objects.update(group=Group.objects.get(name=AppGroup.DEFAULT))


def add_default_group_to_participation(apps, schema_editor):
    Group = apps.get_model("app", "Group")
    Participation = apps.get_model("app", "Participation")
    Participation.objects.update(group=Group.objects.get(name=AppGroup.DEFAULT))


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_partition_task_partition'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='role',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='role',
        ),
        migrations.AddField(
            model_name='invitation',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.AddField(
            model_name='participation',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.RunPython(create_default_group_if_not_exist, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_default_group_to_invitation, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_default_group_to_participation, reverse_code=migrations.RunPython.noop),
        migrations.AlterField(
            model_name='invitation',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.group'),
        ),
    ]
