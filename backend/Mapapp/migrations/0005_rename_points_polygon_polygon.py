# Generated by Django 5.0.1 on 2024-01-09 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mapapp', '0004_alter_polygon_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polygon',
            old_name='points',
            new_name='polygon',
        ),
    ]
