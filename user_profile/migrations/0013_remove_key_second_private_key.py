# Generated by Django 4.0.6 on 2022-08-21 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_rename_keys_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='key',
            name='second_private_key',
        ),
    ]
