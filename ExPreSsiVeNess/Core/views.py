# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import pkg_resources

# Create your views here.


def core(request):
    def load_plugins(tag):
        plugins = {}

        for ep in pkg_resources.iter_entry_points(group=tag):
            p = ep.load()
            print("{} {}".format(ep.name, p))
            plugin = p()

            plugins[ep.name] = plugin

        return plugins

    load_plugins("visualizer")
    return load_plugins("visualizer")['simple_visualizer'].core()
