from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
app.count = 0

@app.route('/')
def index():
    if session.has_key('counter') == False:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template("index.html" , count = session['counter'])

@app.route('/by_two', methods=['POST'])
def count_by_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['counter'] = 0
    return redirect("/")

app.run(debug=True) 