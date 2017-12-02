from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "SecretKey"
import random 

@app.route('/')
def index():
    if 'random' not in  session:
        session['random'] = random.randrange(1,101)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def user_guess():
    userguess = request.form['user_guess']
    print userguess
    
    if int(userguess) > session['random']:
        userguess = "Too high"
        print "Too high!"
        return redirect('/')
    elif int(userguess) < session['random']:
        userguess = "Too low"
        print "Too low!"
        return redirect('/')
    elif int(userguess) == session['random']:
        userguess = "Correct Number"
        print "You got it right!"
        session.pop('random')
        return redirect("/")
    else:
        print "Enter a number from 1 and 100"
        return redirect('/')
    
    # return redirect('/')

app.run(debug=True)

# setting the random number
## allowing the user to make a number guess
## validate the guess
### display the correct box
#### play again buttom