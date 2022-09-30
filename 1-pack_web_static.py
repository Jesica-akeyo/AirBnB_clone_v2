#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder of the AirBnB Clone repo
"""
from fabric.operations import local
from datetime import datetime
import os


def do_pack():
    """ generates a .tgz archive """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception:
        return None
