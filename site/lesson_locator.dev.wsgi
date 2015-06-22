#!/usr/bin/env python
"""
lesson_locator.dev.wsgi

Copyright (c) 2014 Kevin Cureton/Nik Gervae
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import datetime
import logging
import os
import pkgutil
import sys

import pyramid.config
import wsgiref.simple_server

LESSON_LOCATOR_ROOT = os.path.normpath(os.path.join(os.path.dirname(sys.argv[0]), ".."))
sys.path.append(os.path.join(LESSON_LOCATOR_ROOT, "python"))

import lesson_locator.configurator

# ---------------------------------------------------------------------------------------------
# Setup and run the Pyramind WSGI application.
# ---------------------------------------------------------------------------------------------
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

config = lesson_locator.configurator.getPyramidConfigurator(is_dev_server=True)

application = config.make_wsgi_app()

logger.info("Starting simple server on port 8000...")
server = wsgiref.simple_server.make_server('0.0.0.0', 8000, application)
server.serve_forever()
