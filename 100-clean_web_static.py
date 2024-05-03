#!/usr/bin/python3
"""clean"""
from fabric.api import local, env, run
import os


# must be added to work as expected but checked refuse
# versions = os.listdir("versions/")
env.hosts = ['54.165.77.224', '100.24.242.177']


def do_clean(number=0):
    """fabric function"""
    versions_date_time = []
    for ver in versions:
        versions_date_time.append(int(ver.split("_")[2][:-4]))
    versions_date_time.sort()
    if number == "0" or number == "1":
        for ver in versions:
            if str(versions_date_time[-1]) not in ver and \
                 str(versions_date_time[-2]) not in ver:
                local(f"rm -rf versions/{ver}")
                run(f"rm -rf /data/web_static/releases/versions/{ver[:-4]}")
    else:
        for ver in versions:
            in_list = False
            for i in range(1, int(number) * 2 + 1):
                if str(versions_date_time[-i]) in ver:
                    in_list = True
            if not in_list:
                local(f"rm -rf versions/{ver}")
                run(f"rm -rf /data/web_static/releases/versions/{ver[:-4]}")
