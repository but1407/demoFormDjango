# Generated by Django 5.0.3 on 2024-03-13 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_alter_post_time_create"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="time_create",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 3, 13, 16, 46, 0, 593113)
            ),
        ),
    ]
