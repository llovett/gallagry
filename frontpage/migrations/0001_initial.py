# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GalleryLinkPosition'
        db.create_table('frontpage_gallerylinkposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pos_x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pos_y', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rotation', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=5)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('frontpage', ['GalleryLinkPosition'])

        # Adding model 'BlogLinkPosition'
        db.create_table('frontpage_bloglinkposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pos_x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pos_y', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rotation', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=5)),
            ('is_default', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('frontpage', ['BlogLinkPosition'])


    def backwards(self, orm):
        # Deleting model 'GalleryLinkPosition'
        db.delete_table('frontpage_gallerylinkposition')

        # Deleting model 'BlogLinkPosition'
        db.delete_table('frontpage_bloglinkposition')


    models = {
        'frontpage.bloglinkposition': {
            'Meta': {'object_name': 'BlogLinkPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pos_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pos_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rotation': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '5'})
        },
        'frontpage.gallerylinkposition': {
            'Meta': {'object_name': 'GalleryLinkPosition'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'pos_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pos_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rotation': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '5'})
        }
    }

    complete_apps = ['frontpage']