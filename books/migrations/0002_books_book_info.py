# Generated by Django 5.0.2 on 2024-02-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='book_info',
            field=models.TextField(default=''),
        ),
    ]
