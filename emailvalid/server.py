from flask import Flask, request, redirect, render_template, session, flash
import re
emailregex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "this is my secret key"
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/email', methods = ['POST'])
def new_email():
    email=request.form['email']
    if not emailregex.match(email):
        flash('Not a Vaild E-mail!')
        return redirect('/')
    if emailregex.match(email):
        checkquery = mysql.query_db('select * from emails where email_address = "{}"'.format(email))
        #return redirect('/')
        if len(checkquery) > 0:
            flash('This E-Mail already exists')
            return redirect('/')
        else:
            email_query = ('insert into emails (email_address, created_at, updated_at) values ("{}", now(), now())'.format(email))
            mysql.query_db(email_query)
            query = "select * from emails"
            emails = mysql.query_db(query)
            query = "select * from emails"
            emails = mysql.query_db(query)
            flash("The email address you entered ({}) is a valid E-Mail address! Thank you for Registering!".format(email))
            return render_template('success.html' , all_emails = emails)
app.run(debug=True)
