from flask import Flask, request, render_template, redirect
import cgi
import os

import re

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    return render_template('index.html', title = "Sign Up")




@app.route("/signup", methods=['GET','POST'])
def signup():
    Username= request.form['Username']
    password = request.form['Password']
    v_pass = request.form['Verify']
    email = request.form['email']

#intializing all error
    user_error = ''
    pass_error = ''
    verify_error = ''
    email_error = ''

#conditioning for username:
    if Username == "": # validating username
        user_error = "Please enter correct username"
    elif  len(Username) <3 or len(Username)>20:
        user_error = "The username must contain 3 to 20 character"
        Username = ''
    elif ' ' in Username :
        user_error = 'Username cannot contain any spaces'
        Username = ''

#conditioning for password:
    if password == "": # validating password
        pass_error = "Please enter correct password"
    elif  len(password) <=3 or len(password)>=20:
        pass_error = "The password must contain 3 to 20 character"
        password = ''
    elif ' ' in password :
        pass_error = 'Password cannot contain any spaces'
        password = ''

#conditioning for matching verify password and passwrod.
    if v_pass == '':
        verify_error = "Please enter correct matching password"
    elif v_pass != password :
        verify_error = "Password does not match, please try again!"
        v_pass = ''

#email validation:
    if email != "": # Validate Email
        # Used regex for complete email validation.
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) or (len(email)<3 or len(email)>20):
            email_error = "Not a valid email address."


    if not user_error and not pass_error and not verify_error and not email_error:
        return render_template('welcome.html', Username = Username)
    else:
        return render_template(
            'index.html',
            Username = Username,
            user_error = user_error,
            password = password,
            pass_error = pass_error, v_pass=v_pass,
            verify_error = verify_error,
            email = email,
            email_error = email_error
            )

app.run()



        








