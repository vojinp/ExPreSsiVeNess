from django.http import HttpResponse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SimpleVisualizer:
    def __init__(self):
        with open(BASE_DIR + '/simple/templates/index.html', 'r') as f:
            self.template = f.read()

    def get_template(self):
        return self.template
