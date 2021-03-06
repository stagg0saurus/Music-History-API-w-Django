# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('Name', 'Label', 'Year_Released', 'artist')},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('Title', 'artist', 'album', 'genre')},
        ),
        migrations.RenameField(
            model_name='album',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='album_id',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='genre_id',
            new_name='genre',
        ),
    ]
