#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scirius.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    # setup supervisor service
    cmd = '''
        mkdir -p /usr/share/python/scirius
        cp ./usr/share/python/scirius/bin /usr/share/python/scirius
    
        cp ./usr/bin/gunicorn /usr/bin
        chmod 0755 /usr/bin/gunicorn
    '''
    exit_status = subprocess.call(cmd)
