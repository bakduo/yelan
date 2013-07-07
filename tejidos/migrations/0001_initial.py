# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Aguja'
        db.create_table(u'tejidos_aguja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'tejidos', ['Aguja'])

        # Adding model 'Tejido'
        db.create_table(u'tejidos_tejido', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('tipo_lana', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('anotation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('tipo_de_punto', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('ancho', self.gf('django.db.models.fields.FloatField')()),
            ('largo', self.gf('django.db.models.fields.FloatField')()),
            ('punto', self.gf('django.db.models.fields.IntegerField')()),
            ('tejido_finalizado', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('detalle_tejido', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('detalle_fantasia', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('detalle_hilado', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('fleco', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('aguja', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['tejidos.Aguja'], unique=True)),
        ))
        db.send_create_signal(u'tejidos', ['Tejido'])


    def backwards(self, orm):
        # Deleting model 'Aguja'
        db.delete_table(u'tejidos_aguja')

        # Deleting model 'Tejido'
        db.delete_table(u'tejidos_tejido')


    models = {
        u'tejidos.aguja': {
            'Meta': {'object_name': 'Aguja'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'tejidos.tejido': {
            'Meta': {'object_name': 'Tejido'},
            'aguja': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['tejidos.Aguja']", 'unique': 'True'}),
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