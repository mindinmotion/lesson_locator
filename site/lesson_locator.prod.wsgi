#!/usr/bin/env python
"""
lesson_locator.prod.wsgi

Copyright (c) 2014 Kevin Cureton/Nik Gervae
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import os
import sys

import pyramid.config

LESSON_LOCATOR_ROOT = os.path.normpath(os.path.join(os.path.dirname(sys.argv[0]), ".."))
sys.path.append(os.path.join(LESSON_LOCATOR_ROOT, "python"))

import lesson_locator.configurator

# ---------------------------------------------------------------------------------------------
# Setup and run the Pyramind WSGI application.
# ---------------------------------------------------------------------------------------------
config = lesson_locator.configurator.getPyramidConfigurator()
application = config.make_wsgi_app()
