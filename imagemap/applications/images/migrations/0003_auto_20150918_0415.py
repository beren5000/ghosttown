# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import applications.images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=applications.images.models.image_name_images, null=True, verbose_name='image', blank=True),
        ),
    ]
