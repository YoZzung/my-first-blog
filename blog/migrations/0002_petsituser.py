# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetsitUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('password', models.CharField(max_length=50, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('sex', models.CharField(max_length=10, blank=True)),
                ('birth', models.DateField(max_length=50, blank=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
