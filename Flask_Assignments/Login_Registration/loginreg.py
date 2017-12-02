from flask import Flask ,render_template, redirect, request, flash
# import the Connector function
# from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
# import datetime
# connect and store the connection in "mysql" note that you pass the database name to the function
# mysql = MySQLConnector(app, 'makefriendsdb')
# an example of running a query
# print mysql.query_db("SELECT * FROM makefriends")

@app.route('/')
def index():                                      
    return render_template('index.html')   

@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email'].lower()
    # match = re.match()
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    success = False
    # if len(email < 1 or len(first_name ))
    if success True:
        password = md5.new()
    return redirect('/')

app.route('/login', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    return redirect('/')
app.run(debug=True)