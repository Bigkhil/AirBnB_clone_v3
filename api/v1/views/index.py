#!/usr/bin/python3
"""
index.py file
"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", strict_slashes=False)
def status():
    """simple view status"""
    return jsonify({"status": "OK"})
