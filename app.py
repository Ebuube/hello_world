#!/usr/bin/env python3
"""Test app
"""
from flask import Flask, jsonify
from flask_cors import (CORS, cross_origin)

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route('/')
def hello():
    return jsonify({"status": "ok", "note": "Hello, World!"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
