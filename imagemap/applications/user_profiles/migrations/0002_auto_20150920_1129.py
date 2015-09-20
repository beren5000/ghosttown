# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='gender', choices=[(0, 'masculino'), (1, 'femenino')]),
        ),
    ]
