# Generated by Django 4.2.4 on 2023-08-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_userprofile_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('specialization', models.CharField(max_length=30)),
                ('experience', models.FloatField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]