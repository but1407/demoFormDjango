# Generated by Django 5.0.3 on 2024-03-13 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField(max_length=255)),
                (
                    "time_create",
                    models.DateTimeField(
                        default=datetime.datetime(2024, 3, 13, 9, 26, 14, 288294)
                    ),
                ),
            ],
        ),
    ]
