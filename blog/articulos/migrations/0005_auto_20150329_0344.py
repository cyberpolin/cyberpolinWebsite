# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0004_auto_20150301_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='', storage=django.core.files.storage.FileSystemStorage(location='static/2015/03')),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='tipo',
            field=models.ForeignKey(default=2, to='articulos.Tipo'),
            preserve_default=True,
        ),
    ]
