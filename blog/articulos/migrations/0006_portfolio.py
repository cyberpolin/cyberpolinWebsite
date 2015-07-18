# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_auto_20150329_0344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('img', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='static/2015/03'), upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
