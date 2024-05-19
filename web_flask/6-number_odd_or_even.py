#!/usr/bin/python3
"""
this module resolves task 1 per requirements more details in the readme file.
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def murugo():
    """ this is my home function for task 0. """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def muhanda_1():
    """ this is the route for hbnb. """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def muhanda_2(text):
    """
    this responds to task 2 where a route portion is kept and displayed.
    """
    under_replace = text.replace('_', ' ')
    return 'C {}'.format(under_replace)


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def muhanda_3(text):
    """
    this responds to task 3 where a route portion is kept and displayed.
    """
    under_replace = text.replace('_', ' ')
    return 'Python {}'.format(under_replace)


@app.route('/number/<int:n>', strict_slashes=False)
def umubare(n):
    """
    task 4 ireba niba n ari integer then it prints it.
    """
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """ task 6 for odd or even number. """
    e_or_o = "even" if n % 2 == 0 else "odd"
    val = (
        "bare" : n,
        "e_or_o" : e_or_o
    )
    return render_template("6-number_odd_or_even.html", val)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
