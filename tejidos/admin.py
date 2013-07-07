'''
#############################################################################
#                                                                           #
#   Clase admin para tejidos                                                #
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

from django.contrib import admin
from tejidos.models import Tejido, Aguja, Archivos, Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ['mail','fecha']

class ArchivosAdminInline(admin.StackedInline):
    model = Archivos
    extra = 1

class AgujaInline(admin.StackedInline):
    model = Aguja
    extra = 0
#    fk_name = 'tejido'

class TejidoAdmin(admin.ModelAdmin):
    list_display = ('title','tipo_lana','description','ancho','largo','punto','tipo_de_punto',)
    list_filter = ('title','tipo_lana','fecha_inicio','punto','tipo_de_punto',)
    fieldsets = (
          (None, {
              'fields': (('title','fecha_inicio'), 'description', 
              ('tipo_lana','tag','tipo_de_punto'))
          }),
    )
    search_filter = ['title','tipo_lana' ,'anotation', 'description','fecha_inicio']
    inlines = [AgujaInline,ArchivosAdminInline]
    class Media:
        js = ('js/tinymce/tinymce.min.js',
              'js/basic_config.js',)

admin.site.register(Message, MessageAdmin)
admin.site.register(Tejido, TejidoAdmin)
admin.site.register(Aguja)
