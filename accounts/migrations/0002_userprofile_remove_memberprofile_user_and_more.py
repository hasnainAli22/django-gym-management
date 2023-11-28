# Generated by Django 4.2.7 on 2023-11-20 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(blank=True, max_length=20)),
                ('preferences', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='memberprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='trainerprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AdminProfile',
        ),
        migrations.DeleteModel(
            name='MemberProfile',
        ),
        migrations.DeleteModel(
            name='TrainerProfile',
        ),
    ]