from os import path, mkdir

from flask import Flask, render_template

from config import LOGS_FOLDER
from main.main import main_blueprint, posts_blueprint
from search.search import search_blueprint
from user_feed.user_feed import user_feed_blueprint

if not path.exists(LOGS_FOLDER):
    mkdir(LOGS_FOLDER)

app = Flask(__name__, template_folder='templates')

app.register_blueprint(main_blueprint)
app.register_blueprint(posts_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
