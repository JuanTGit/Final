from app import app
from flask import render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.forms import RegisterForm, LoginForm
from app.models import User

@app.route('/')
def index():
    my_name = "Juan"
    my_hometown = "Houston"
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    person = {
        'name': 'Jack Man',
        'age': 18,
        'best_friend': 'Bob Fuller'
    }
    return render_template('index.html', name=my_name, city=my_hometown, colors=colors, person=person)


@app.route('/name')
@login_required
def name():
    my_name = "Juan"
    return render_template("name.html", name=my_name)


@app.route("/test")
def test():
    return "<h1>This is a test!</h1>"

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #Get data from form
        username = form.username.data
        email = form.email.data
        password = form.password.data

        # Check if username or email is already in db
        user_exists  = User.query.filter((User.username == username)|(User.email == email)).all()
        #if it is, return back to register
        if user_exists:
            return redirect(url_for('register'))
        
        # Create a new user instance using form data
        new_user = User(username=username, email=email, password=password)

        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab data from form
        username = form.username.data
        password = form.password.data
        # Query user table for user with username
        user = User.query.filter_by(username=username).first()
        # if the user doesn't exist or incorrect password
        if not user or not user.check_password(password):
            # Redirect to login
            print('That username or password is incorrect')
            return redirect(url_for('login'))
        # if user does exist and correct password, log user in
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))