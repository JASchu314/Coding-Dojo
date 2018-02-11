from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "This is hidden"
@app.route('/')

def form():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def returnform():
    session['yourname'] = request.form['yourname']
    session['Dojo-Location'] = request.form["Dojo-Location"]
    session['Favorite-Language'] = request.form['Favorite-Language']
    session['comment'] = request.form['comment']
    return render_template('users.html')
app.run(debug=True)