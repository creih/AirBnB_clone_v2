#!/usr/bin/python3
"""
this module resolves task 1 per requirements more details in the readme file.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def murugo():
    """ this is my home function for task 0. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def muhanda_1():
    """ this is the route for hbnb. """
    return 'HBNB'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
