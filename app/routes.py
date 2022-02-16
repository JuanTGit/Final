from app import app
from flask import render_template

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
def name():
    my_name = "Juan"
    return render_template("name.html", name=my_name)


@app.route("/test")
def test():
    return "<h1>This is a test!</h1>"