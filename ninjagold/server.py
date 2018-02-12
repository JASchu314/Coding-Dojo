from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "This is hidden"

@app.before_first_request
def createvars():
    session['goldcount'] = 0
    session['log'] = ''

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/process_money' , methods = ['POST'])
def Farm():
    if request.form['building'] == 'farm':
        session['gold'] = random.randrange(10 , 21)
        session['goldcount'] += session['gold']
        session['log'] += 'The Farm has given you {} Gold!  '.format(session['gold'])+str(datetime.datetime.now()) + '\n'
    if request.form['building'] == 'cave':
        session['gold'] = random.randrange(5 , 11)
        session['goldcount'] += session['gold']
        session['log'] += 'You have found {} Gold in the dark spooky cave.  '.format(session['gold'])+str(datetime.datetime.now()) + '\n'
    if request.form['building'] == 'house':
        session['gold'] = random.randrange(2 , 6)
        session['goldcount'] += session['gold']
        session['log'] += 'You found {} Gold Cleaning the House! Grats!  '.format(session['gold'])+str(datetime.datetime.now()) + '\n'
    if request.form['building'] == 'casino':
        session['gold'] = random.randrange(-50 , 51)
        session['goldcount'] += session['gold']
        if session['goldcount'] > 0:
            if session['gold'] > 0:
                session['log'] += 'You won {} Gold at the Casino, Ya Lucky Duck!  '.format(session['gold']) +str(datetime.datetime.now()) + '\n'
            elif session['gold'] == 0:
                session['log'] += 'You Broke even at the Casino, Try again for a win!  ' +str(datetime.datetime.now()) +'\n'
            elif session['gold'] < 0:
                session['log'] += 'you lost {} Gold at the Casino, Better try again!  ' .format(session['gold']) +str(datetime.datetime.now())
        elif session['goldcount'] < 0:
            session['goldcount'] =0
            session['log'] += "you've gone broke at the Casino, Come back and try again when you have more Gold! " +str(datetime.datetime.now()) + '\n'
    return redirect('/')

app.run(debug=True)