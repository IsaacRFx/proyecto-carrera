# Generated by Django 4.1.1 on 2023-05-10 06:18

import api.utils.upload
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='last name')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('role', models.PositiveIntegerField(choices=[(1, 'Administrator'), (2, 'Collaborator'), (3, 'Student')], default=3, verbose_name='user role')),
                ('is_validated', models.BooleanField(default=False, verbose_name='is validated user')),
                ('identifier_number', models.PositiveIntegerField(unique=True, verbose_name='user id number')),
                ('profile_picture', models.ImageField(default=None, upload_to=api.utils.upload.get_file_path, verbose_name='user picture')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('not_specified', 'Not specified')], default='not_specified', max_length=15, verbose_name='user gender')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]