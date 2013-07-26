# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.sold'
        db.add_column('galleries_image', 'sold',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Image.sold'
        db.delete_column('galleries_image', 'sold')


    models = {
        'galleries.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['settings.BackgroundImage']", 'null': 'True', 'blank': 'True'}),
            'colorscheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['settings.ColorScheme']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'galleries.image': {
            'Meta': {'object_name': 'Image'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['galleries.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'sold': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
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
            'title': ('django.db.models.fields.CharField', [], {'default': "'Color scheme from 25/07/2013 at 07:57 PM'", 'max_length': '200'}),
            'use_for_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_galleries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_mainpage': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['galleries']