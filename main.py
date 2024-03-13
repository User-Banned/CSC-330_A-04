from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add/<num1>/<num2>')
def add_nums(num1, num2):
    if num1.isdigit()==num2.isdigit()==True:
        res=str(int(num1)+int(num2))
        return render_template('add.html',num1=num1,num2=num2,res=res)
    else:
        return render_template('nonDigit.html')
    
@app.route('/sub/<num1>/<num2>')
def sub_nums(num1, num2):
    if num1.isdigit()==num2.isdigit()==True:
        res=str(int(num1)-int(num2))
        return render_template('subtract.html',num1=num1,num2=num2,res=res)
    else:
        return render_template('nonDigit.html')

@app.route('/mult/<num1>/<num2>')
def mult_nums(num1, num2):
    if num1.isdigit()==num2.isdigit()==True:
        res=str(int(num1)*int(num2))
        return render_template('multiply.html',num1=num1,num2=num2,res=res)
    else:
        return render_template('nonDigit.html')
    
@app.route('/divd/<num1>/<num2>')
def divd_nums(num1, num2):
    if num1.isdigit()==num2.isdigit()==True:
        if int(num2) == 0:
            res=num2
        else:
            res=str(float(num1)/int(num2))
        return render_template('divide.html',num1=num1,num2=num2,res=res)
    else:
        return render_template('nonDigit.html')
    