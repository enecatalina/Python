from flask import Flask, render_template , request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user", methods = ['POST'])
def create_user():
    print "Welcome friend!"
    name = request.form['name']
    email = request.form['email']
    print "Name: {}".format(name)
    return render_template("/")
app.run(debug=True)