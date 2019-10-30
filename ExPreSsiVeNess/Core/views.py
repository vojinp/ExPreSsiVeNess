# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from services import plugin_loader
# Create your views here.


def index(request):
    visualizers = plugin_loader.load_plugins("visualizer")
    parsers = plugin_loader.load_plugins("parser")
    # html = plugin_loader.load_plugins("visualizer")['simple_visualizer'].get_template()
    # f = open('./Core/templates/temp.html', 'w')
    # f.write(html)
    # f.close()

    return render(request, 'index.html', {'parsers': parsers, 'visualizers': visualizers})
