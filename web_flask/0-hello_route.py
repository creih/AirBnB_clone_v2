#!/usr/bin/python3
"""
this module resolves task 1 per requirements more details in the readme file
"""
from flask import Flask

app = Flask(__name__)



@app.route('/', strict_slashes=False)
def murugo():
    """ this is my home function for task 0"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
