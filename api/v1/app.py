#!/usr/bin/python3
"""App instance of Flask"""


from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown_appcontext():
    """Calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def errorhandler():
    """Not found"""
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    import os
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
