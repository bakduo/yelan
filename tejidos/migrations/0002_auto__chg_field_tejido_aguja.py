# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tejido.aguja'
        db.alter_column(u'tejidos_tejido', 'aguja_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tejidos.Aguja'], unique=True))

    def backwards(self, orm):

        # Changing field 'Tejido.aguja'
        db.alter_column(u'tejidos_tejido', 'aguja_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tejidos.Aguja'], unique=True))

    models = {
        u'tejidos.aguja': {
            'Meta': {'object_name': 'Aguja'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'tejidos.tejido': {
            'Meta': {'object_name': 'Tejido'},
            'aguja': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tejidos.Aguja']", 'unique': 'True'}),
            'ancho': ('django.db.models.fields.FloatField', [], {}),
            'anotation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'detalle_fantasia': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'detalle_hilado': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'detalle_tejido': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            'fleco': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'largo': ('django.db.models.fields.FloatField', [], {}),
            'punto': ('django.db.models.fields.IntegerField', [], {}),
            'tejido_finalizado': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'tipo_de_punto': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tipo_lana': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['tejidos']