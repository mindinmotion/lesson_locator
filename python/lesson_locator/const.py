#!/usr/bin/env python
"""
lesson_locator/const.py

Values that are read-only during any given application run. Think of this as code-level
configuration that doesn't change very often.

Copyright (c) 2015 Mind In Motion
"""
# ---------------------------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------------------------
import os
import sys

# ---------------------------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------------------------

# -----------------------------------------------------
# The root of the Lesson Locator project. This should
# be populated by the executing script (or WSGI app).
# -----------------------------------------------------
LESSON_LOCATOR_ROOT = None


# ---------------------------------------------------------------------------------------------
# Module test harness
# ---------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is the test harness for the module")
    sys.exit(0)
