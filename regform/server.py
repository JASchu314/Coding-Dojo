from flask import Flask, render_template, request, redirect, session , flash
import re
emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
nameregex = re.compile(r'^[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "This is hidden"

@app.route('/')

def page():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def fieldcheck():
    if len(request.form['email']) < 1:
        flash('We need a vaild E-mail please!')
    elif not emailregex.match(request.form['email']):
        flash('E-mail invalid, Please enter a vaild E-mail')
    elif len(request.form['firstname']) < 1:
        flash('Please enter your first name')
    elif not nameregex.match(request.form['firstname']):
        flash('First name must be alphabetical characters only')
    elif len(request.form['lastname']) <1:
        flash('Please enter your last name')
    elif not nameregex.match(request.form['lastname']):
        flash('Last name must be alphabetical characters only')
    elif len(request.form['password1']) < 9:
        flash('Password must be at least 8 characters')
    elif request.form['password1'] != request.form['password2']:
        flash('Passwords DO NOT match, Please make sure they do :)')
    else:
        flash("Thank You for Registering! Registering for things is important! (but this form isn't)")
    return redirect('/')
app.run(debug=True)