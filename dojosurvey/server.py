from flask import Flask, render_template, request, redirect, session , flash

app = Flask(__name__)
app.secret_key = "This is hidden"
@app.route('/')

def form():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def returnform():
    if len(request.form['yourname']) < 1:
        flash('Name cannot be Empty!')
        return redirect('/')
    elif len(request.form['comment']) > 120:
        flash('Comments cannot exceed 120 characters')
        return redirect('/')
    elif len(request.form['comment']) < 1:
        flash('We need your feedback! Please Leave a Comment!')
        return redirect('/')
    else:
        session['yourname'] = request.form['yourname']
        session['Dojo-Location'] = request.form["Dojo-Location"]
        session['Favorite-Language'] = request.form['Favorite-Language']
        session['comment'] = request.form['comment']
        return render_template('users.html')
app.run(debug=True)