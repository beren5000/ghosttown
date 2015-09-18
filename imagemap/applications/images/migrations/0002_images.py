# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import applications.images.models
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(upload_to=applications.images.models.image_name, null=True, verbose_name='image', blank=True)),
                ('caption', models.CharField(max_length=50, null=True, verbose_name='caption', blank=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_images_images_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_images_images_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]
