# Generated by Django 4.1.1 on 2023-06-01 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_kudertest'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningTypeTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('result', models.CharField(choices=[('visual', 'Visual'), ('auditivo', 'Auditivo'), ('kinestesico', 'Kinestésico')], max_length=50, verbose_name='result')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]