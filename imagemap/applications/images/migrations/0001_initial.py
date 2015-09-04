# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import geoposition.fields
import applications.images.models
import audit_log.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(upload_to=applications.images.models.image_name, null=True, verbose_name='image', blank=True)),
                ('position', geoposition.fields.GeopositionField(max_length=42, verbose_name='map_position')),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_images_uploadedimages_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_images_uploadedimages_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
                ('user_profile', models.ForeignKey(verbose_name='user_profile', to='user_profiles.UserProfile')),
            ],
            options={
                'verbose_name': 'uploaded_image',
                'verbose_name_plural': 'uploaded_images',
            },
        ),
    ]
