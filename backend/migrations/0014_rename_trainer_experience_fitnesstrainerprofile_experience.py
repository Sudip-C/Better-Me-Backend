# Generated by Django 4.2.4 on 2023-08-30 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_rename_experience_fitnesstrainerprofile_trainer_experience'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fitnesstrainerprofile',
            old_name='trainer_experience',
            new_name='experience',
        ),
    ]