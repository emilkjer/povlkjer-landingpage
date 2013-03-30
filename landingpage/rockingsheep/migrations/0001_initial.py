# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Email'
        db.create_table(u'rockingsheep_email', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('send_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('send_address', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'rockingsheep', ['Email'])


    def backwards(self, orm):
        # Deleting model 'Email'
        db.delete_table(u'rockingsheep_email')


    models = {
        u'rockingsheep.email': {
            'Meta': {'object_name': 'Email'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'send_address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['rockingsheep']