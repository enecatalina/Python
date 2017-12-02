from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def hello_world():
  return 'Hello World! My Name is Catalina'  

@app.route('/aboutme')
def aboutme():
    return "I am a python web developer and love walking."

@app.route('/projects')
def projects():
    return "My Projects: - Danger Zones - Fat Unicorn: The poopening - my Cohort"

app.run(debug=True)  

## Dojo Solution example##
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/projects')
# def projects():
#     my_projects = ['Ninja Gold', 'Great Number Game', 'Disappearing Ninjas', 'Dojo Survey']
#     return render_template('projects.html', projects=my_projects)

# @app.route('/about')
# def about():
#     return render_template('about.html')

# app.run(debug=True)