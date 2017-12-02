
from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
   name = request.form['name']
   if len(request.form['name']) == 0:
       flash('Name cannot be empty!')
       return redirect('/')
   else:
        pass
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   return render_template('results.html', name = name, location = location, language = language, comment = comment)

app.run(debug=True) 