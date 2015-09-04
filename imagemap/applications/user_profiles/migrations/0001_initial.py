# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import audit_log.models.fields
import applications.user_profiles.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=90, verbose_name='name')),
                ('abbr', models.CharField(max_length=10, verbose_name='abbr')),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_user_profiles_documenttype_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_user_profiles_documenttype_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
            ],
            options={
                'verbose_name': 'document_type',
                'verbose_name_plural': 'document_types',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, null=True, editable=False)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, null=True, editable=False)),
                ('description', models.CharField(max_length=255, null=True, verbose_name='description', blank=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('avatar', models.ImageField(upload_to=applications.user_profiles.models.avatar_image_name, null=True, verbose_name='avatar', blank=True)),
                ('about_me', models.TextField(max_length=220, null=True, verbose_name='about_me', blank=True)),
                ('document_id', models.IntegerField(null=True, verbose_name='document_id', blank=True)),
                ('gender', models.SmallIntegerField(blank=True, null=True, verbose_name='gender', choices=[(0, 'male'), (1, 'female'), (2, 'gender_other')])),
                ('telephone', models.IntegerField(null=True, verbose_name='telephone', blank=True)),
                ('cellphone', models.BigIntegerField(null=True, verbose_name='cellphone', blank=True)),
                ('address', models.TextField(null=True, verbose_name='address', blank=True)),
                ('birth_date', models.DateField(null=True, verbose_name='birth_date', blank=True)),
                ('created_by', audit_log.models.fields.CreatingUserField(related_name='created_user_profiles_userprofile_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('document_type', models.ForeignKey(verbose_name='document_type', blank=True, to='user_profiles.DocumentType', null=True)),
                ('modified_by', audit_log.models.fields.LastUserField(related_name='modified_user_profiles_userprofile_set', editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='modified by')),
                ('user', models.OneToOneField(related_name='profile', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user_profile',
                'verbose_name_plural': 'user_profiles',
            },
        ),
    ]
