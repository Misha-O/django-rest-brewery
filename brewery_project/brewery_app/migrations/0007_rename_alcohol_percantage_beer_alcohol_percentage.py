# Generated by Django 4.0.1 on 2022-01-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_app', '0006_remove_beer_ingredient_hop_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beer',
            old_name='alcohol_percantage',
            new_name='alcohol_percentage',
        ),
    ]
