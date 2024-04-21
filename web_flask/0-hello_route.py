#!/usr/bin/python3
"""
A script to start flask and the application must be 
listening on port 5000 host 0.0.0.0
"""

from flask import Flask

app = Flask(__name__)

#define the route for the task roor URL'/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello BNB'
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    """
    Start Flask Dev Server
    lsiten on the network infrastructure required
    """

    app.run(host='0.0.0.0', port=5000)
