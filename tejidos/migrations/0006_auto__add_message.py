# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'tejidos_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('tema', self.gf('django.db.models.fields.CharField')(max_length=110)),
            ('mail', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'tejidos', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'tejidos_message')


    models = {
        u'tejidos.aguja': {
            'Meta': {'object_name': 'Aguja'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'tejido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tejidos.Tejido']", 'null': 'True', 'blank': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'tejidos.archivos': {
            'Meta': {'object_name': 'Archivos'},
            'archivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'descript': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fk_tejido': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tejidos.Tejido']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'tejidos.message': {
            'Meta': {'ordering': "['fecha']", 'object_name': 'Message'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'tema': ('django.db.models.fields.CharField', [], {'max_length': '110'}),
            'texto': ('django.db.models.fields.TextField', [], {})
        },
        u'tejidos.tejido': {
            'Meta': {'object_name': 'Tejido'},
            'ancho': ('django.db.models.fields.FloatField', [], {}),
            'anotation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'fleco': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.FloatField', [], {}),
            'punto': ('django.db.models.fields.IntegerField', [], {}),
            'tag': ('tagging_autocomplete.models.TagAutocompleteField', [], {'null': 'True'}),
            'tipo_de_punto': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tipo_lana': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['tejidos']