# Generated by Django 4.1.7 on 2023-03-09 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0002_rename_nodes_notes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'verbose_name': 'notes', 'verbose_name_plural': 'notes'},
        ),
    ]
