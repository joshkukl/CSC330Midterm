from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html')

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'The sum of {num1} and {num2} is {result}'

@app.route('/substract/<int:num1>/<int:num2>')
def substract(num1, num2):
    result = num1 - num2
    return f'The difference of {num1} and {num2} is {result}'

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return f'The product of {num1} and {num2} is {result}'

@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    result = num1 / num2
    return f'The quotient of {num1} and {num2} is {result}'