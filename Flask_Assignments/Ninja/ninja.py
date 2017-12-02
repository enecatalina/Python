from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/selected_ninja')
def selected_ninja():
    return render_template("selected_ninja.html")

app.run(debug=True)