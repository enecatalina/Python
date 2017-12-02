from flask import Flask ,render_template, redirect, request, flash
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 
# import datetime
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'makefriendsdb')
# an example of running a query
print mysql.query_db("SELECT * FROM makefriends")

@app.route('/')
def index():                                      
    return render_template('index.html')   

@app.route('/create_friends', methods=['POST'])
def create_friend():
    error = True
    first_name = request.form['first_name']
    if len(request.form['first_name']) < 1:
        error = False
        flash('You need to fill out your first name')
    last_name = request.form['last_name']
    if len(request.form['last_name']) < 1:
        error = False
        flash('You need to fill out your last name')
    occupation = request.form['occupation']
    if len(request.form['occupation']) < 1:
        error = False
        flash('You need to fill out your occupation')
    if error == True:
        flash('Thank you!')
        mysql.query_db("INSERT INTO makefriends (first_name,last_name,occupation) VALUES ('{}','{}','{}')".format(first_name,last_name,occupation))
        # created_at = datetime.datetime.now()
    return redirect('/')
  
   

app.run(debug=True)



# ## def process ():
# # errors = []
# ## if there is a problem:
#     errors.appead(message)
# if another problem:
#     erros.appead(message)
# if len(errors) > 0 
# GIVE ERRORS TO USERS
# else 
#     create the profile 