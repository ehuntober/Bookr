# Generated by Django 4.1.7 on 2023-03-19 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor_review_bookcontributors_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookContributors',
            new_name='BookContributor',
        ),
    ]
