# Generated by Django 4.1.7 on 2023-04-03 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auths", "0004_primary_is_lecturer_primary_staff_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="primary", old_name="staff_number", new_name="staff_id",
        ),
    ]
