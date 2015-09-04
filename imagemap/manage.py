#!/usr/bin/env python
import os
import sys
try:
    from rol import settings_name
except ImportError:
    settings_name = "settings"

settings_var = "imagemap."+settings_name
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_var)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
