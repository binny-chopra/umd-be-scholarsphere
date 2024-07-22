from app import app
from model.sponsors_model import sponsors_model
from flask import request, make_response

obj = sponsors_model()

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

@app.route("/sponsors", methods=["GET", "OPTIONS"])
def registered_sponsors_controller():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    return obj.sponsors_list_model()

@app.route("/sponsors/new", methods=["POST", "OPTIONS"])
def new_sponsor_controller():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    return obj.new_sponsor_model(request.get_json())

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE,OPTIONS")
    return response
