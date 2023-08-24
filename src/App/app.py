from flask import Flask, render_template
from src.Logging.logger import custom_logger

logger = custom_logger(__file__)
app = Flask(__name__)

@app.route('/')
def index():
    logger.info('user has reached index page')
    return render_template('index.html')

# @app.route('/<usr_name>')
def user(usr_name):
    logger.info(f'{usr_name} has accessed their personal space.')
    return render_template('user.html', name = usr_name)

app.add_url_rule('/<usr_name>','user page',user)