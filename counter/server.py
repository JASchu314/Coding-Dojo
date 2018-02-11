from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "This is hidden"

@app.before_first_request
def addcount():
    session['count'] = 0
@app.route('/')
def page():
    session['count'] += 1
    return render_template('index.html')

app.run(debug=True)