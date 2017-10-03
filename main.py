from flask import Flask, render_template, request, redirect


app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/")
def user_signup():
    return render_template("index.html")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    user_name = request.form["username"] 
    user_error = ''

    password = request.form["password"]
    password_error = ''

    verify = request.form['verify']
    verify_error = ''

    email = request.form['email']
    email_error = ''

    if user_name == "":
        user_error = "Please enter a valid username."
    else:
        user_name = user_name

    if len(user_name) < 3 or len(user_name) > 20:
        user_error = "Please enter a valid username"

    else:
        user_name = user_name

    if len(password) < 3 or len(password) > 20:
        password_error = "Please enter a valid password"
        
    if verify != password:
        verify_error = "Passwords must match!"
        
    
    if email != '':
        if ' ' in email:
            email_error = "Please enter a valid email address"
        if "@" not in email:
            email_error = "Please enter a valid email address"
        if "." not in email:
            email_error = "Please enter a valid email address"

    if not user_error and not password_error and not verify_error and not email_error:
        return render_template('confirmation.html', user_name = user_name)
    else:
        return render_template('index.html', user_error = user_error, password_error = password_error, verify_error = verify_error, email_error = email_error, name = user_name, email = email)

app.run()