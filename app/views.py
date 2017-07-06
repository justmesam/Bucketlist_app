""" This are the handlers that respond to the web browsers"""

from flask import render_template
from app import app

@app.route('/')
def index():
    """renders the homepage of the app"""
    return render_template('index.html')
