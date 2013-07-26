# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BackgroundImage.use_for_blog'
        db.add_column('settings_backgroundimage', 'use_for_blog',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'ColorScheme.use_for_blog'
        db.add_column('settings_colorscheme', 'use_for_blog',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BackgroundImage.use_for_blog'
        db.delete_column('settings_backgroundimage', 'use_for_blog')

        # Deleting field 'ColorScheme.use_for_blog'
        db.delete_column('settings_colorscheme', 'use_for_blog')


    models = {
        'settings.backgroundimage': {
            'Meta': {'object_name': 'BackgroundImage'},
            'background_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'full_height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'full_width': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'use_for_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_galleries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_mainpage': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'settings.colorscheme': {
            'Meta': {'object_name': 'ColorScheme'},
            'background_color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'foreground_color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'rollover_color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Color scheme from 01/07/2013 at 04:38 PM'", 'max_length': '200'}),
            'use_for_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_galleries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_mainpage': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['settings']