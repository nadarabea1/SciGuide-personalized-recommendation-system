# Generated by Django 4.1.7 on 2023-03-09 19:46

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nodes',
            new_name='Notes',
        ),
    ]