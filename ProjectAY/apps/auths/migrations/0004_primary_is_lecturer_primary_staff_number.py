# Generated by Django 4.1.7 on 2023-04-03 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auths", "0003_alter_primary_course"),
    ]

    operations = [
        migrations.AddField(
            model_name="primary",
            name="is_lecturer",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="primary",
            name="staff_number",
            field=models.CharField(max_length=50, null=True),
        ),
    ]