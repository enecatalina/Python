from flask import Flask ,render_template, redirect, request
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
import datetime
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'makefriendsdb')
# an example of running a query
print mysql.query_db("SELECT * FROM makefriends")

@app.route('/')
def index():                        
    makefriends = mysql.query_db("SELECT * FROM makefriends")               
    return render_template('index.html',friends=makefriends)   

@app.route('/create_friends', methods=['POST'])
def create_friend():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    occupation = request.form['occupation']
    created_at = datetime.datetime.now()
    mysql.query_db("INSERT INTO makefriends (first_name,last_name,occupation,created_at) VALUES ('{}','{}','{}','{}')".format(first_name,last_name,occupation,created_at))
    print first_name,last_name,occupation
    return redirect('/')

app.run(debug=True)