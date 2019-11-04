from django.http import HttpResponse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ComplexVisualizer:
    def __init__(self):
        with open(BASE_DIR + '/complex/templates/index.html', 'r') as f:
            self.template = f.read()

    def get_template(self):
        return self.template
