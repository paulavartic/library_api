# Generated by Django 5.1.4 on 2024-12-22 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookissue',
            name='return_date',
            field=models.DateField(default=datetime.date(2025, 1, 6), verbose_name='Return date'),
        ),
    ]