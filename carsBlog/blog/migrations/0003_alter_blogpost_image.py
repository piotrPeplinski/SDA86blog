# Generated by Django 5.1.2 on 2024-11-17 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogpost_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]