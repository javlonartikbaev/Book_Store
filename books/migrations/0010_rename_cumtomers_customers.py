# Generated by Django 5.0.2 on 2024-02-23 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0009_books_genre_alter_genre_slug"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cumtomers",
            new_name="Customers",
        ),
    ]
