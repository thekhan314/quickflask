from app import app
from flask import render_template

@app.route('/')
def home():
    return "Hello World!"

@app.route('/john')
def john():

    john = {'name':'John',
        'age':32,
        'favfood':'Cake'}

    return render_template('base.html',user=john)

@app.route('/phill')
def phill():

    phill = {'name':'Phill',
         'age':36,
         'favfood':'Pizza'}

    return render_template('base.html',user=phill)