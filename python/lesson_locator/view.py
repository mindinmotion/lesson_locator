#!/usr/bin/env python
"""
view.py

The views for the Felden Lesson Locator site.

Copyright (c) 2015 Mind In Motion
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import datetime
import json
import os
import string

import pyramid.renderers
import pyramid.view


# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------------
# View methods
# ---------------------------------------------------------------------------------------------
@pyramid.view.view_config(route_name='index')
def indexPage(request):
    """
    The index (starting) page for the Feldenkrais Lesson Locator.
    """
    response = pyramid.renderers.render_to_response("lesson_locator:site/index.jinja2",
                                                    dict(),
                                                    request=request)
    return response



# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is the test harness for the module")
    sys.exit(0)
