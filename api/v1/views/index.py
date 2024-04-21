#!/usr/bin/python3
"""Index.py"""


from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route('/status')
def status():
    """status"""
    return jsonify({"status": "OK"})
