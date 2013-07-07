#from django.conf.urls.defaults import *
'''
#############################################################################
#                                                                           #
#   url para tejidos                                                        #
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

from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from tejidos.models import Tejido, Aguja, Archivos
from tejidos.views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.global_settings import STATICFILES_DIRS, MEDIA_ROOT

urlpatterns = patterns('tejidos.views',
             #url(r'^$','index',name='index'),
             (r'^$',IndexView.as_view()),
             (r'^home/$',IndexView.as_view()),
             url(r'^ver_tejido/(?P<id>\d+)/$','ver_detalle',name='ver_detalle_por_id'),
             url(r'^tejido/(?P<title>[-\w]+)/$','ver_tejido',name='ver_detalle_por_nombre'),
             url(r'^tagging_autocomplete/',include('tagging_autocomplete.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
