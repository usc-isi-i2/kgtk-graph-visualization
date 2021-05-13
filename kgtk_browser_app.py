import flask
import requests
from flask import render_template, jsonify

from app_config import host, port


# How to run:
# > export FLASK_APP=kgtk_browser_app.py
# > export FLASK_ENV=development
# > flask run


### Flask application

app = flask.Flask(__name__)
app.static_url_path='/static'


### URL handlers:

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/<node_no>', methods=['GET'])
def api(node_no):
    response = requests.get("https://dsbox02.isi.edu:8888/kgtk-browser/kgtk/browser/backend/get_all_node_data?node={node_no}&lang=en&images=true&fanouts=true".format(node_no=node_no))
    return jsonify(response.json())

@app.route('/search/<search_text>', methods=['GET'])
def search(search_text):
    response = requests.get("https://kgtk.isi.edu/api?q={search_text}&extra_info=true&language=en&is_class=false&type=ngram&size=5".format(search_text=search_text))
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(host=host, port=port)
