from django.http import HttpResponse
import os
import zipfile

from django.shortcuts import render

class SimpleVisualizer:
    def __init__(self):
        pass

    def get_template(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        f = open(BASE_DIR + '/simple/templates/index.html', 'r')

        return f.read()
