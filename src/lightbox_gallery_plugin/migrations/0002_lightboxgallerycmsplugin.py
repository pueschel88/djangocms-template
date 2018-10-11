# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-12 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('lightbox_gallery_plugin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightboxGalleryCmsPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='lightbox_gallery_plugin_lightboxgallerycmsplugin', serialize=False, to='cms.CMSPlugin')),
                ('thumbnail_size', models.CharField(blank=True, choices=[('50x50', 'Small (50px)'), ('100x100', 'Medium (100px)'), ('150x150', 'Big (150px)')], default='50x50', max_length=256, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]