# Standard library imports
import json 
# Remote library imports
from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/data', methods=['GET'])
def all_data():
    try:
        with open('db.json') as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "data not found"}), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)