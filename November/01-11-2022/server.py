from flask import Flask, render_template
import math

app = Flask(__name__)

"""SIMPLE CALULATOR"""

@app.route('/simple_cal')
def simple_cal():
    return render_template('simple_cal.html')

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return f'ADDITION OF {num1} + {num2} = {str(num1+num2)}'

@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1,num2):
    return f'SUBTRACTION OF {num1} - {num2} = {str(num1-num2)}'

@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1,num2):
    return f'MULTIPLICATION OF {num1} x {num2} = {str(num1 * num2)}'

@app.route('/div/<int:num1>/<int:num2>')
def div(num1,num2):
    return f'DIVISION OF {num1} / {num2} = {str(num1/num2)}'

""" Mathrmatical cal """

@app.route('/math_cal')
def home():
    return render_template('math_cal.html')

@app.route('/double/<int:num>')
def double(num):
    return f'DOUBLE OF {num} IS {str(num*2)}'
 
@app.route('/square/<int:num>')
def square(num):
    return f'SQUARE OF {num} IS {str(num*num)}'

@app.route('/cube/<int:num>')
def cube(num):
    return f'CUBE OF {num} IS {str(num*num*num)}'

@app.route('/root/<int:num>')
def root(num):
    return f'SQUARE ROOT OF {num} IS {math.sqrt(num)}'


app.run()