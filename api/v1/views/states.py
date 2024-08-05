#!/usr/bin/python3
"""
this is a handler for all states api actions
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models.state import State
from models import storage

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """retrieve all the states"""
    states = storage.all(State).values()
    states_list = [state.to_dict() for state in states]
    return jsonify(states_list)
