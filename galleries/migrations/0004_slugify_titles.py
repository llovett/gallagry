# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        """Turns the titles of Images and Galleries into strings that are URL-safe"""
        # Note: Don't use "from appname.models import ModelName". 
        # Use orm.ModelName to refer to models in this application,
        # and orm['appname.ModelName'] for models in other applications.
        from galleries.utils import slugify
            
        for gallery in orm.Gallery.objects.all():
            gallery.title_slug = slugify(gallery.title)
            gallery.save()
        for image in orm.Image.objects.all():
            image.title_slug = slugify(image.title)
            image.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        for gallery in orm.Gallery.objects.all():
            gallery.title_slug = None
            gallery.save()
        for image in orm.Image.objects.all():
            image.title_slug = None
            image.save()

    models = {
        'galleries.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'background_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['settings.BackgroundImage']", 'null': 'True', 'blank': 'True'}),
            'colorscheme': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['settings.ColorScheme']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'title_slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'})
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
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'title_slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'}),
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
            'title': ('django.db.models.fields.CharField', [], {'default': "'Color scheme from 14/08/2013 at 10:39 PM'", 'max_length': '200'}),
            'use_for_blog': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_galleries': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'use_for_mainpage': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['galleries']
    symmetrical = True
