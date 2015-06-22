#!/usr/bin/env python
"""
lesson_locator/configurator.py

The Pyramid configurator object for the site.

Copyright (c) 2015 Mind In Motion
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import datetime
import json
import os
import string

import pyramid.config
import pyramid.renderers
import pyramid.view

import lesson_locator

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
# Configuratored Things
# ---------------------------------------------------------------------------------------------
def getPyramidConfigurator(is_dev_server=False):
    """
    Get a pre-configurated Pyramid WSGI application.
    """
    # Configure and create the WSGI application.
    config = pyramid.config.Configurator()

    # Configuration settings.
    settings = dict()

    if is_dev_server:
        settings['pyramid.reload_templates'] = True

    config.add_settings(settings)

    # Include additional pyramid modules.
    config.include('pyramid_jinja2')

    # Scan the code for view declarations.
    config.scan(lesson_locator)

    # Setup the views.
    config.add_route('index', '/')

    # Setup the APIs.
    config.add_route('api.lessons', '/api/lessons')
    config.add_route('api.lesson', '/api/lesson/{lesson_id}')

    # Setup the static content.
    config.add_static_view("js", "lesson_locator:site/js/")
    config.add_static_view("snipets", "lesson_locator:site/snipets/")
    config.add_static_view("static", "lesson_locator:site/static/")
    config.add_static_view("styles", "lesson_locator:site/styles/")

    return config


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is the test harness for the module")
    sys.exit(0)
