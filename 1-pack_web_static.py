#!/usr/bin/env python3

from fabric.api import *
from datetime import datetime
import os


def do_pack():
    try:
        the_time = datetime.now()
        time_string = the_time.strftime("%Y%m%d%H%M%S")
        if os.path.isdir("versions") is False:
            local("mkdir versions")
        local(
            f"sudo tar -cvzf versions/web_static_{time_string}.tgz web_static")
        f_path = f"versions/web_static_{time_string}.tgz"
        f_size = os.path.getsize(f_path)
        print(f"web_static packed: {f_path} -> {f_size}")
        return (f_path)
    except CommandFailed:
        return None


do_pack()
