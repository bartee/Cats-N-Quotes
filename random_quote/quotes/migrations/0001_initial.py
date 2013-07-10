# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table(u'quotes_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comeback', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('original_author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'quotes', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table(u'quotes_quote')


    models = {
        u'quotes.quote': {
            'Meta': {'object_name': 'Quote'},
            'comeback': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original_author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'quote': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['quotes']