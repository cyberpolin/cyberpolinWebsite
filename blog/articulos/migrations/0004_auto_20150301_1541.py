# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='alt',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='caption',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='latlon',
            field=models.CharField(null=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(null=True, max_length=100),
            preserve_default=True,
        ),
    ]
