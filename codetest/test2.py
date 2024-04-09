#!/usr/bin/env python3

from fabric.api import *
from datetime import datetime


def do_pack():
    the_time = datetime.now()
    time_string = the_time.strftime("%Y%m%d%H%M%S")
    print(time_string)
    local(f"sudo tar -cvzf versions/web_static_{time_string}.tgz web_static")


do_pack()
