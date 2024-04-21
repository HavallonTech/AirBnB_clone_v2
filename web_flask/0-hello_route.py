#!/usr/bin/python3
"""
A script to start flask and the application must be 
listening on port 5000 host 0.0.0.0
"""

from flask import flask

app = Flask(__name__)

#define the route for the task roor URL'/'
@app.route('/', start_slashes=False)
deg hello_hbnb():
    """
    Display 'Hello BNB'
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    #Start Flask Dev Server
    #lsiten on the network infrastructure required
    app.run(host='0.0.0.0', port=5000)
