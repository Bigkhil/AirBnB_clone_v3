#!/usr/bin/python3
"""
this is app.py
"""

from os import getenv
from models import storage
from flask import Flask, jsonify, make_response
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def tear_down(exception):
    """this method closes the database connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for error pages"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(
            host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', '5000')),
            threaded=True
            )
