# Generated by Django 5.0.1 on 2024-01-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alertapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertmodel',
            name='alert_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
