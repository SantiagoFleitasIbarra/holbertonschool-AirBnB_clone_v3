#!/usr/bin/python3

from api.v1.views import app_views
import json

@app_views.route('/status')
def status():
    dict = {
        "status": "OK"
    }
    return json.dumps(dict)
