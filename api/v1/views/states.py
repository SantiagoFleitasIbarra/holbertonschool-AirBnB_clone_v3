#!/usr/bin/python3
"""
Paths for managing State items and actions
"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def fetch_all_states():
    """
    Retrieves all State items
    """
    states_list = []
    for state_obj in storage.all(State).values():
        states_list.append(state_obj.to_dict())
    return jsonify(states_list), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def add_state():
    """
    Create state path
    """
    state_data = request.get_json()
    if not state_data:
        abort(400, {"Not a JSON"})
    if "name" not in state_data:
        abort(400, {"Missing name"})

    new_state = State(**state_data)
    storage.new(new_state)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def fetch_state_by_id(state_id):
    """
    Retrieves a specific State item by ID
    """
    state_item = storage.get(State, state_id)
    if state_item:
        return jsonify(state_item.to_dict()), 200
    else:
        abort(404)


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state_by_id(state_id):
    """
    Updates a specific State item by ID
    """
    state_item = storage.get(State, state_id)
    if not state_item:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    update_data = request.get_json()
    for key, value in update_data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state_item, key, value)
    storage.save()
    return jsonify(state_item.to_dict()), 200


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def remove_state_by_id(state_id):
    """
    Deletes State item by ID
    """
    state_item = storage.get(State, state_id)
    if state_item:
        storage.delete(state_item)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)
