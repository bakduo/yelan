# -*- coding: utf-8 -*-

'''
#############################################################################
#                                                                           #
#   modelos para tejidos                                                    #
#   Copyright (C) 2013 linuxknow                                            #
#   linuxknow [at] gmail dot com                                            #
#   This program is free software: you can redistribute it and/or modify    #
#   it under the terms of the GNU General Public License as published by    #
#   the Free Software Foundation, either version 3 of the License, or       #
#   (at your option) any later version.                                     #
#                                                                           #
#   This program is distributed in the hope that it will be useful,         #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#   GNU General Public License for more details.                            #
#                                                                           #
#   You should have received a copy of the GNU General Public License       #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>    #
#                                                                           #
#############################################################################
'''


from django.db import models
from django.db.models import permalink
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
from tagging_autocomplete.models import TagAutocompleteField

import os

def get_file_path(instance,filename):
    return os.path.join(instance.fileDir,filename)

class Tejido(models.Model):
    title = models.CharField('Título',max_length=250,help_text='Ingrese un título al tejido')
    tipo_lana = models.CharField('Tipo Lana',max_length=250,help_text='Ingrese el tipo de tejido')
    description = models.TextField('Descripcion de tejido', help_text='Ingrese alguna descripción del tejido',null=True,blank=True)
    anotation = models.TextField('Anotación de tejido',help_text='Ingrese alguna notación de tejido',null=True,blank=True)
    tipo_de_punto = models.CharField(max_length=250,null=True,blank=True)
    ancho = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(100)])
    largo = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(100)])
    punto = models.IntegerField()
    #tejido_finalizado = models.ImageField(upload_to=get_file_path, blank=True)
    #detalle_tejido =  models.ImageField(upload_to=get_file_path, blank=True)
    #detalle_fantasia =  models.ImageField(upload_to=get_file_path, blank=True)
    #detalle_hilado =  models.ImageField(upload_to=get_file_path, blank=True)
    fecha_inicio = models.DateTimeField('Fecha inicio')
    fecha_fin = models.DateTimeField('Fecha fin',null=True,blank=True)
    fleco = models.BooleanField()
    fecha = models.DateTimeField(auto_now=True)
    tag = TagAutocompleteField('Tags',help_text="Separa con coma(,)",null=True,blank=True)

    def get_primer_imagen(self):
          adjunto = Archivos.objects.filter(fk_tejido__id=self.id)[:1]
          print adjunto[0]
          return adjunto[0].archivo
   
    def __unicode__(self):
        return u'%s' % (self.title)

    def adjunto(self):
        adjunto = Archivos.objects.filter(fk_tejido__id=self.id)
        return adjunto

    def get_absolute_url(self):
        return '/tejido/%s/' % (self.title)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name=u'Tejido'
        verbose_name_plural=u'Tejidos'
#    @permalink
#    def get_absolute_url(self):
#        return ('view_knitting', None, {'knitting':self.title})

class Aguja(models.Model):

    tipo = models.CharField('Tipo',max_length=250,help_text='Ingrese el tipo de aguja')

    numero = models.IntegerField()

    tejido = models.ForeignKey(Tejido,null=True,blank=True)

    def __unicode__(self):
        return u'%s | %s' % (self.tipo, self.numero)

    def __str__(self):
        return u'%s | %s' % (self.tipo, self.numero)

class Archivos(models.Model):
    nombre = models.CharField('Nombre Archivo',max_length=250,help_text='Archivo')
    descript = models.TextField('Descripcion de adjunto', help_text='Ingrese alguna descripción del adjunto',null=True,blank=True)
    archivo = models.FileField(upload_to=get_file_path,blank=True)
    fk_tejido = models.ForeignKey(Tejido)
    fileDir = 'archivos/'

    def __unicode__(self):
        return u'%s' % (self.nombre)

    class Meta:
        verbose_name = u'Subir archivos'

class Message(models.Model):
    nombre = models.CharField(max_length=30)
    tema = models.CharField(max_length=110)
    mail = models.EmailField()
    fecha = models.DateTimeField(auto_now=True)
    texto = models.TextField(validators=[MaxLengthValidator(400)])

    def __unicode__(self):
        return u'%s' % (self.tema)

    class Meta:
        ordering = ['fecha']
