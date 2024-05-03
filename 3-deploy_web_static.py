#!/usr/bin/python3
"""
creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import local, put, run, env
from datetime import datetime
import os


env.hosts = ['100.24.242.177', '54.165.77.224']


def do_pack():
    """fabric function"""
    tgz_name = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    result = local("tar -cvz web_static -f versions/web_static_{}.tgz".format(
        tgz_name))
    if result.succeeded:
        return ("versions/web_static_{}.tgz".format(tgz_name))
    else:
        return None


def do_deploy(archive_path):
    """fabric function"""
    tar_name = archive_path.split("/")[1]
    var = "/data/web_static/releases/"
    if not os.path.exists(archive_path):
        return False
    name_without_tgz = archive_path[:-4]
    try:
        put(archive_path, "/tmp/")
        local("cp {} /tmp/".format(archive_path))
        run("mkdir -p /data/web_static/releases/{}/".format(name_without_tgz))
        run("tar -xzC /data/web_static/releases/{} -f /tmp/{}".format(
            name_without_tgz, tar_name))
        run("rm /tmp/{}".format(tar_name))
        run("mv {}{}/web_static/* {}{}/".format(
            var, name_without_tgz, var, name_without_tgz))
        run("rm -rf {}{}/web_static".format(var, name_without_tgz))
        run("rm -f /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(
            var, name_without_tgz))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """archive and distribute"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return (do_deploy(archive_path))
