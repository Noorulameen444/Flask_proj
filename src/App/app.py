from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/<usr_name>')
def user(usr_name):
    return render_template('user.html', name = usr_name)

app.add_url_rule('/<usr_name>','user page',user)