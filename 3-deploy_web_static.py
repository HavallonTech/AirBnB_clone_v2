#!/usr/bin/env python3
"""
Fabric script to generate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
fab -f 3-deploy_web_static.py deploy -i ~/.ssh/school -u ubuntu
"""

from datetime import datetime
from fabric.api import *
import os
from os.path import exists
env.hosts = ['52.91.147.146', '3.85.16.39']
env.user = "ubuntu"
env.key_filename = '~/.ssh/school'

def do_pack():
    """
    making an archive on web_static folder
    """

    try:
        time = datetime.now()
        the_archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
        if os.path.isdir("version") is False:
            local('mkdir -p versions')
        create = local(f'tar -cvzf versions/{the_archive} web_static')
        if create is not None:
            return archive
    except:
        return None


def do_deploy_none(archive_path):
    """distributes an archive to a web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
def do_deploy():
    if os.path.exists(archive_path) is False:
        print("Warning no file to compress")
        return False

    # Get the name
    new_path = archive_path.split("/")[-1]
    # Get the name of the archive without extension
    folder = new_path.split('.')[0]

    # upload the archive
    if put(archive_path, "/tmp/{}".
            format(new_path)).failed is True:
        return False
    # Creating the right path
    if run("rm -rf /data/web_static/releases/{}/".
            format(folder)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(folder)).failed is True:
        return False
    # uncompress
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(new_path, folder)).failed is True:
        return False
    # remove the archive
    if run("rm  /tmp/{}".format(new_path)).failed is True:
        return False
    # move the content of web_static from uncompress folder
    if run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".
            format(folder, folder)).failed is True:
        return False

    # delete the symbolic link
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    # Remove content of web_static from uncompress folder
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(folder)).failed is True:
        return False
    # create a new symoblic link
    if run("ln -sf /data/web_static/releases/{} /data/web_static/current".
            format(folder)).failed is True:
        return False

    print("New version deployed!")
    return True
