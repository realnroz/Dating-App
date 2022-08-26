# Generated by Django 4.0.6 on 2022-08-21 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0010_alter_userconnection_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private_key', models.TextField(blank=True, null=True)),
                ('second_private_key', models.TextField(blank=True, null=True)),
                ('public_key', models.TextField(blank=True, null=True)),
                ('keys_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='keys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
