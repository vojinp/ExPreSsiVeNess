# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from services import plugin_loader
import os
import json
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    visualizers = plugin_loader.load_plugins("visualizer")
    parsers = plugin_loader.load_plugins("parser")
    return render(request, 'index.html', {"visualizers": visualizers})


def showVisualizer(request, visualizer):
    visualizers = plugin_loader.load_plugins("visualizer")
    parsers = plugin_loader.load_plugins("parser")
    print(str(visualizer))
    data = parsers['json_parser'].load(BASE_DIR + '/test_file.json')

    template = visualizers[str(visualizer)].get_template()
    with open('./Core/templates/temp.html', 'w') as f:
        f.write(template)

    return render(request, 'temp.html', {"data": json.dumps(data), "visualizers": visualizers})

