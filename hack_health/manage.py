#!/usr/bin/env python
import os
import sys
import pywapi as weather


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hack_health.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
