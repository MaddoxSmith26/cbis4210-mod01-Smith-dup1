from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/ireland')
def ireland():
    return render_template('ireland.html')

@app.route('/germany')
def germany():
    return render_template('germany.html')

@app.route('/france')
def france():
    return render_template('france.html')
