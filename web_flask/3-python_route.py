#!/usr/bin/python3
"""
A script to start flask and the application must be
listening on port 5000 host 0.0.0.0
"""

from flask import Flask

app = Flask(__name__)


"""define the route for the task roor URL'/'
"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello BNB'
    """
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def c_and_text(text):
    """
    Display 'C followed by the text passed as variable'
    Replace underscore with the text variable
    """
    text_formatted = text.replace('_', ' ')
    return f"C {text_formatted}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def python_and_text(text):
    """
    Display 'C followed by the text passed as variable'
    Replace underscore with the text variable
    """
    text_formatted = text.replace('_', ' ')
    return f"Python {text_formatted}"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB'
    """
    return "HBNB"


if __name__ == "__main__":
    """
    Start Flask Dev Server
    lsiten on the network infrastructure required
    """

    app.run(host='0.0.0.0', port=5000)
