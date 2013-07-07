# Create your views here.
'''
#############################################################################
#                                                                           #
#   vista para tejidos                                                      #
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


from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from tejidos.models import Tejido, Aguja, Archivos, Message
from tejidos.forms import MessageForm
from django.views.generic import TemplateView
from django.core.mail import send_mail

import os

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        tejido = Tejido.objects.all()
        form = MessageForm(initial={'nombre': 'nombre', 'mail': 'mail', 'texto':'texto', 'tema': 'tema'})
        data = {
            'form': form,
        }

        return render_to_response(self.template_name,RequestContext(request, locals()))
        

    def post(self, request):
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        data = {
            'form': form,
        }

        return render_to_response(self.template_name,RequestContext(request, locals()))

        
        
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tejido'] = Tejido.objects.all()
        return context

def get_file_path(instance,filename):
    return os.path.join(instance.fileDir,filename)

def index(request):
    tejido = Tejido.objects.all()
    return render_to_response('index.html',RequestContext(request, locals()))

def ver_detalle(request,id):
    ver = get_object_or_404(Tejido,id=id)
    return render_to_response('tejido/ver.html', RequestContext(request, locals()))

def ver_tejido(request,title):
    ver = get_object_or_404(Tejido,title=title)
    return render_to_response('tejido/ver.html', RequestContext(request, locals()))

def ver_archivo(request,path):
    print path
