# Generated by Django 4.0.1 on 2022-01-13 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_app', '0004_hop_malt_water_remove_beer_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='ingredient_water',
            field=models.CharField(default='spring water', max_length=60),
        ),
        migrations.AlterField(
            model_name='hop',
            name='beer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hop', to='brewery_app.beer'),
        ),
        migrations.AlterField(
            model_name='malt',
            name='beer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='malt', to='brewery_app.beer'),
        ),
        migrations.AlterField(
            model_name='water',
            name='beer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='water', to='brewery_app.beer'),
        ),
    ]
