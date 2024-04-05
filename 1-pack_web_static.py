#!/usr/bin/python3
# create a .tgz archive that collect all web_static files
from fabric.api import local
from datetime import datetime


def do_pack():
    """pack the files in web_static folder"""
    path = 'versions'
    local(f'mkdir -p {path}')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path += f'/web_static_{date}.tgz'
    cmd = local(f'tar -cvzf {path} web_static/')
    return path if cmd.succeeded else None
