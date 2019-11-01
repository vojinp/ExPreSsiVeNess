# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from services import plugin_loader
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    visualizers = plugin_loader.load_plugins("visualizer")
    parsers = plugin_loader.load_plugins("parser")

    json = parsers['json_parser'].load(BASE_DIR + '/test_file.json')
    print(json)

    return render(request, 'index.html', {'parsers': parsers, 'visualizers': visualizers})
