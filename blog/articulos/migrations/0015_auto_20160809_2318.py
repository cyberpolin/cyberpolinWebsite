# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-09 23:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0014_auto_20160809_2317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='fecha_psql',
            new_name='fecha',
        ),
    ]
