# Generated by Django 4.1.7 on 2023-03-25 09:59

import cloudinary_storage.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="students.course",
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="note_file",
            field=models.FileField(
                null=True,
                storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(),
                upload_to="",
            ),
        ),
        migrations.AlterField(
            model_name="topic", name="notes", field=models.TextField(null=True),
        ),
    ]
