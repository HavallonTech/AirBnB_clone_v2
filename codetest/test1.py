#!/usr/bin/env python3
"""
Testing fabric codes
"""

# from fabric import run, local

from fabric.api import run, local

# Replace 'hostname' and 'username' with your actual values
# conn = Connection(host='localhost', user='kestplanet')

result = local("mkdir -p mytest/test/code")
local("mkdir -p data/web_static/releases/test/")
local("mkdir -p data/web_static/current")
if result.succeeded:
    print("ok")
else:
    print("not ok")
