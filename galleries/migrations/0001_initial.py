# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table('galleries_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('gallery', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['galleries.Gallery'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('for_sale', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('galleries', ['Image'])

        # Adding model 'Gallery'
        db.create_table('galleries_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('preview_image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('background_image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['settings.BackgroundImage'], null=True, blank=True)),
            ('colorscheme', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['settings.ColorScheme'], null=True, blank=True)),
        ))
        db.send_create_signal('galleries', ['Gallery'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('galleries_image')

        # Deleting model 'Gallery'
        db.delete_table('galleries_gallery')


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
            'title': ('django.db.models.fields.CharField', [], {'default': "'Color scheme from 25/07/2013 at 07:55 PM'", 'max_length': '200'}),
            'use_for_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_galleries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_mainpage': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['galleries']