# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Archivos'
        db.create_table(u'tejidos_archivos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('descript', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('archivo', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('fk_tejido', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tejidos.Tejido'])),
        ))
        db.send_create_signal(u'tejidos', ['Archivos'])

        # Deleting field 'Tejido.tejido_finalizado'
        db.delete_column(u'tejidos_tejido', 'tejido_finalizado')

        # Deleting field 'Tejido.detalle_hilado'
        db.delete_column(u'tejidos_tejido', 'detalle_hilado')

        # Deleting field 'Tejido.detalle_tejido'
        db.delete_column(u'tejidos_tejido', 'detalle_tejido')

        # Deleting field 'Tejido.detalle_fantasia'
        db.delete_column(u'tejidos_tejido', 'detalle_fantasia')


    def backwards(self, orm):
        # Deleting model 'Archivos'
        db.delete_table(u'tejidos_archivos')

        # Adding field 'Tejido.tejido_finalizado'
        db.add_column(u'tejidos_tejido', 'tejido_finalizado',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Tejido.detalle_hilado'
        db.add_column(u'tejidos_tejido', 'detalle_hilado',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Tejido.detalle_tejido'
        db.add_column(u'tejidos_tejido', 'detalle_tejido',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Tejido.detalle_fantasia'
        db.add_column(u'tejidos_tejido', 'detalle_fantasia',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)


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
            'tipo_de_punto': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'tipo_lana': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['tejidos']