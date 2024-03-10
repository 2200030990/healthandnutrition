# Generated by Django 5.0 on 2024-03-10 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_health_meditation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fitness',
            old_name='Style',
            new_name='TimetoVisit',
        ),
        migrations.RenameField(
            model_name='fitness',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='Style',
            new_name='TimetoVisit',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='place',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='meditation',
            old_name='Style',
            new_name='TimetoVisit',
        ),
        migrations.RenameField(
            model_name='meditation',
            old_name='place',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='nutrition',
            old_name='HowtoReach',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='fitness',
            name='Attractions',
        ),
        migrations.RemoveField(
            model_name='health',
            name='Attractions',
        ),
        migrations.RemoveField(
            model_name='health',
            name='title',
        ),
        migrations.RemoveField(
            model_name='meditation',
            name='Attractions',
        ),
        migrations.RemoveField(
            model_name='meditation',
            name='title',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='Attractions',
        ),
        migrations.RemoveField(
            model_name='nutrition',
            name='title',
        ),
    ]