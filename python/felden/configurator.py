#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------
"""
felden/configurator.py

The Pyramid configurator object for the site.

Copyright (c) 2014 Next Education LLC
"""
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# TODO
#
# ---------------------------------------------------------------------------------------------

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

import felden

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
    config.scan(felden)

    # Setup the views.
    config.add_route('index', '/')

    # Setup the APIs.
    config.add_route('api.lessons', '/api/lessons')
    config.add_route('api.lesson', '/api/lesson/{lesson_id}')

    # Setup the static content.
    config.add_static_view("js", "felden:site/js/")
    config.add_static_view("snipets", "felden:site/snipets/")
    config.add_static_view("static", "felden:site/static/")
    config.add_static_view("styles", "felden:site/styles/")

    return config


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print "This is the test harness for the module"
    sys.exit(0)
