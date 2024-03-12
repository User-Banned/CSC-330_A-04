from flask import Flask, render_template
app = Flask(__name__)

@app.route('/add/<num1>/<num2>')
def add_nums(num1, num2):
    return render_template('add.html',num1=num1,num2=num2)

@app.route('/sub/<num1>/<num2>')
def sub_nums(num1, num2):
    return render_template('subtract.html',num1=num1,num2=num2)

@app.route('/mult/<num1>/<num2>')
def mult_nums(num1, num2):
    return render_template('multiply.html',num1=num1,num2=num2)

@app.route('/divd/<num1>/<num2>')
def divd_nums(num1, num2):
    return render_template('divide.html',num1=num1,num2=num2)
