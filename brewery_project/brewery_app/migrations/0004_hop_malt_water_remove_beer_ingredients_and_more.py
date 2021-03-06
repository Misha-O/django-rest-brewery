# Generated by Django 4.0.1 on 2022-01-13 12:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brewery_app', '0003_alter_ingredient_hop_alter_ingredient_malt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False, verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Malt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=60)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False, verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='spring water', editable=False, max_length=60)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now, editable=False, verbose_name='created_at')),
            ],
        ),
        migrations.RemoveField(
            model_name='beer',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='beer',
            name='ingredient_hop',
            field=models.CharField(default='type of hop', max_length=60),
        ),
        migrations.AddField(
            model_name='beer',
            name='ingredient_malt',
            field=models.CharField(default='type of malt', max_length=60),
        ),
        migrations.AddField(
            model_name='beer',
            name='ingredient_water',
            field=models.CharField(default='type of water', max_length=60),
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.AddField(
            model_name='water',
            name='beer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewery_app.beer'),
        ),
        migrations.AddField(
            model_name='malt',
            name='beer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewery_app.beer'),
        ),
        migrations.AddField(
            model_name='hop',
            name='beer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brewery_app.beer'),
        ),
    ]
