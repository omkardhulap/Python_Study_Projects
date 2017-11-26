'''
Created on Oct 30, 2017

@author: omkar.d
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask, render_template, request  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/request1')   # URL '/' to be handled by main() route handler
def servie1():
    """Say hello"""
    return 'Hello, world!'

@app.route('/request2')   # URL '/' to be handled by main() route handler
def servie2():
    """Say hello"""
    return 'Hello, omkar!'

@app.route('/request3')   # URL '/' to be handled by main() route handler
def servieJson():
    """Say hello"""
    return '{"users": [{"id": 0,"name": "Adam Carter","work": "Unilogic","email": "adam.carter@unilogic.com","dob": "1978","address": "83 Warner Street","city": "Boston","optedin": true},{"id": 1,"name": "Leanne Brier","work": "Connic","email": "leanne.brier@connic.org","dob": "13/05/1987","address": "9 Coleman Avenue","city": "Toronto","optedin": false}],"images": ["img0.png","img1.png","img2.png"],"coordinates": {    "x": 35.12,    "y": -21.49},"price": "$59,395"}'

import time
@app.route('/request4')   # URL '/' to be handled by main() route handler
def servieHTML():
    """Say hello"""
    return render_template('myfile.html', title='Omkar', mytime=str(time.asctime( time.localtime())))

@app.route('/input')
def renderInput():
    'http://localhost:5000/input?filename=myfile.html'
    if 'filename' in request.args:
        myfilename = request.args.get('filename')
        return render_template(myfilename)
    else:
        return "No input file specified"
    
@app.route('/input/<string(length=2):filename>',methods=['GET'])
def renderValidInput(filename):
    'http://localhost:5000/input/myfile.html'
    if 'filename' in request.view_args:
        myfilename = request.view_args['filename']
        print('myfilename abc>> ' + myfilename)
        return render_template(myfilename)
    else:
        return "No input file specified"
    
@app.route('/input/<string:filename>',methods=['GET'])
def renderInputPage(filename):
    'http://localhost:5000/input/myfile.html'
    if 'filename' in request.view_args:
        myfilename = request.view_args['filename']
        print('myfilename abc>> ' + myfilename)
        return render_template(myfilename)
    else:
        return "No input file specified"

if __name__ == '__main__':  # Script executed directly?
    #app.run(host='localhost', port='5555', debug=True)()  # Launch built-in web server and run this Flask webapp
    app.run()()
    