from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "This is hidden"
@app.route('/')

def page():
    return render_template("index.html")

@app.route('/ninja')
def ninjas():
    return render_template("ninja.html")

@app.route('/ninja/<color>' , methods=['GET'])
def ninjacolor(color):
    if color == 'blue':
        return render_template('/ninja.html' , color ='blue')
    elif color == 'orange':
        return render_template('/ninja.html' , color = 'orange')
    elif color == 'red':
        return render_template('/ninja.html' , color = 'red')
    elif color == 'purple':
        return render_template('/ninja.html' , color = 'purple')
    else:
        return render_template('/ninja.html' , color = 'april')

app.run(debug=True)