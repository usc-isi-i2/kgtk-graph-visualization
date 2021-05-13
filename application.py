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

@app.route('/<node>', methods=['GET'])
def index(node):
    return render_template("index.html", value = node)


@app.route('/api/<node_no>', methods=['GET'])
def api(node_no):
    response = requests.get("https://dsbox02.isi.edu:8888/kgtk-browser/kgtk/browser/backend/get_all_node_data?node={node_no}&lang=en&images=true&fanouts=true".format(node_no=node_no))
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host=host, port=port)
