# Generated by Django 5.1.3 on 2024-11-25 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_book_authors_remove_book_genre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='is_collected',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reserved_until',
        ),
        migrations.AddField(
            model_name='reservation',
            name='expires_at',
            field=models.DateTimeField(default=20241202),
            preserve_default=False,
        ),
    ]
