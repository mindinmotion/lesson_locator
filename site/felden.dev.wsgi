#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------
"""
felden.dev.wsgi

Copyright (c) 2014 Kevin Cureton/Nik Gervae
"""
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# TODO
# ---------------------------------------------------------------------------------------------

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


# ---------------------------------------------------------------
# Configure the Python environment
# ---------------------------------------------------------------
sys.path.append("/Users/kcureton/Documents/work/felden/python")
sys.path.append("/Users/nik/Programming/felden/python")

import felden.configurator


# ---------------------------------------------------------------------------------------------
# Setup and run the Pyramind WSGI application.
# ---------------------------------------------------------------------------------------------
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

config = felden.configurator.getPyramidConfigurator(is_dev_server=True)

application = config.make_wsgi_app()

logger.info("Starting simple server on port 8000...")
server = wsgiref.simple_server.make_server('0.0.0.0', 8000, application)
server.serve_forever()
