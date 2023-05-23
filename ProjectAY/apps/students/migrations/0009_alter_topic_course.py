# Generated by Django 4.1.7 on 2023-05-21 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0008_remove_course_topic_topic_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="course",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="students.course",
            ),
        ),
    ]