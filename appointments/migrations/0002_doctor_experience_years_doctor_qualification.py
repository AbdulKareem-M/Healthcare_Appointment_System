# Generated by Django 5.1.4 on 2025-05-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='experience_years',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='qualification',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
