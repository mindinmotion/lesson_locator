#!/usr/bin/env python
# ---------------------------------------------------------------------------------------------
"""
felden.prod.wsgi

Copyright (c) 2014 Kevin Cureton/Nik Gervae
"""
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# TODO
# ---------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import os
import sys

import pyramid.config


# ---------------------------------------------------------------
# Configure the Python environment
# ---------------------------------------------------------------
sys.path.append("/var/www/code/felden/python")

import felden.configurator


# ---------------------------------------------------------------------------------------------
# Setup and run the Pyramind WSGI application.
# ---------------------------------------------------------------------------------------------
config = felden.configurator.getPyramidConfigurator()
application = config.make_wsgi_app()
