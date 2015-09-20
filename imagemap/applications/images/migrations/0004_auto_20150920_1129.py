# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20150918_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimages',
            name='user_profile',
            field=models.ForeignKey(verbose_name='user_profile', blank=True, to='user_profiles.UserProfile', null=True),
        ),
    ]
