# Generated by Django 5.0.1 on 2024-01-25 22:10

import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mapapp', '0008_servicearea_delete_customerpolygon_delete_polygon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicearea',
            name='id',
        ),
        migrations.AddField(
            model_name='servicearea',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 1, 25, 21, 0, 8, 276215, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicearea',
            name='date_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='object_version',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='servicearea',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
