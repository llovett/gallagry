# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImageFrame'
        db.create_table('imagespace_imageframe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100)),
            ('manual_positioning', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pos_x', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pos_y', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('width', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('geometry', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('for_sale', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('imagespace', ['ImageFrame'])


    def backwards(self, orm):
        # Deleting model 'ImageFrame'
        db.delete_table('imagespace_imageframe')


    models = {
        'imagespace.imageframe': {
            'Meta': {'object_name': 'ImageFrame'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'for_sale': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'geometry': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'manual_positioning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pos_x': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pos_y': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['imagespace']