#!/usr/bin/python3
# create a .tgz archive that collect all web_static files

from fabric.api import local, task
from datetime import datetime


def do_pack():
    """a fabric script that collect files"""
    path = 'versions'
    local(f'mkdir -p {path}')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    date += f'/web_static_{path}.tgz'
    command = local(f'tar -czf {path} web_static/')
    return path if command.succeeded else None
