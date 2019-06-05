#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTING_MODULE", "helloworld.settings")

    from django.core.management import excute_from_command_line

    excute_from_command_line(sys.argv)
