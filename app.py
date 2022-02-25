from flask import Flask, render_template,url_for, redirect, request
app = Flask(__name__)
from main import *

@app.route('/', methods=['POST','GET'])
def index():
    if request.method =='POST':
        creditor = request.form['creditor']
        amount = request.form['amount']
        borrower = request.form['borrower']
        write_block(creditor,amount,borrower)
        return  redirect(url_for('index'))
    return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check_block():
    results = chek()
    return render_template('check.html', results=results)


if __name__=='__main__':
    app.run(debug=True)