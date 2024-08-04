#!/usr/bin/python3
"""
index.py file
"""

from api.v1.views import app_views
from flask import jsonify
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"amenities": Amenity, "cities": City,
           "places": Place, "reviews": Review, "states": State, "users": User}


@app_views.route("/status", strict_slashes=False)
def status():
    """simple view status"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def stats():
    obj = {}
    "view stats of each object type"
    for key, value in classes.items():
        obj[key] = models.storage.count(value)
    return jsonify(obj)
