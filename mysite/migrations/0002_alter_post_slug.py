# Generated by Django 4.2.6 on 2023-10-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mysite", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=250, unique_for_date="publish"),
        ),
    ]