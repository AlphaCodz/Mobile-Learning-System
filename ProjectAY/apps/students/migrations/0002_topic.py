# Generated by Django 4.1.7 on 2023-03-25 09:03

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
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
                ("name", models.CharField(max_length=200)),
                (
                    "note_file",
                    models.FileField(
                        storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                        upload_to="",
                    ),
                ),
                ("notes", models.TextField()),
            ],
        ),
    ]
