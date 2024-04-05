#!/usr/bin/python3
# create a fabric script that disrbuit

from fabric.api import env, put, run, local, runs_once, task
from datetime import datetime
from os.path import exists

env.hosts = ['18.207.112.142', '100.25.110.244']

@runs_once
def do_pack():
    """pack the files in web_static folder"""
    path = 'versions'
    local('mkdir -p {}'.format(path))
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path += '/web_static_{}.tgz'.format(date)
    cmd = local('tar -cvzf {} web_static/'.format(path))
    return path if cmd.succeeded else None


@task
def do_deploy(archive_path):
    """distribute an archive to web servers"""
    if not (archive_path and exists(archive_path)):
        return False
    path = put(archive_path, '/tmp/')
    if path.failed:
        return False
    outdir = '/data/web_static/releases/'
    link = '/data/web_static/current'
    outdir += path[0].split('/')[-1].split('.')[0]
    if run('mkdir -p {}'.format(outdir)).failed:
        return False
    if run('tar -xzf {} --directory {}'.format(path[0], outdir)).failed:
        return False
    if run('rm -rf {}'.format(path[0])).failed:
        return False
    if run('rm -rf {}'.format(link)).failed:
        return False
    if run('ln -sf {} {}'.format(outdir, link)).failed:
        return False
    if run('mv -n ' + outdir + '/web_static/* ' + outdir).failed:
        return False
    print('New version deployed!\n')
    return True
