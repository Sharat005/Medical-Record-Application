# Generated by Django 3.2.3 on 2021-06-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0002_auto_20210605_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='bp_medicine',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='record',
            name='copd',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='record',
            name='copd_flare',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
