# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 21:11
from __future__ import unicode_literals

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0011_auto_20160407_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='texto',
            field=froala_editor.fields.FroalaField(),
        ),
    ]