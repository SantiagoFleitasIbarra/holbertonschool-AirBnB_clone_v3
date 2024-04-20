#!/usr/bin/python3
"""Index.py"""


from api.v1.views import app_views
import json


@app_views.route('/status')
def status():
    dict = {
        "status": "OK"
    }
    return json.dumps(dict)
