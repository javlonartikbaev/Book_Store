# Generated by Django 5.0.2 on 2024-02-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_books_slug_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='slug_book',
            new_name='slug',
        ),
    ]
