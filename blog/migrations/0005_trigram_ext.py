# Generated by Django 5.0.8 on 2024-08-16 07:31
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_tags"),
    ]

    operations = [
        TrigramExtension()
    ]